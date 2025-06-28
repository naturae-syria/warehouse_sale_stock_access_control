# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    """Class to add fields in sale order line and automatically display the
    value in the fields if we select a product."""

    _inherit = "sale.order.line"

    qty_available = fields.Float(
        string="On Hand Quantity", help="Count of on hand quantity"
    )
    forecast_quantity = fields.Float(
        string="Forecast Quantity", help="Count of forecast quantity"
    )

    @api.onchange("product_id")
    def _onchange_product_id(self):
        """Function to set the value of the fields based on product."""
        product_restriction = tools.str2bool(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("sale_stock_restrict.product_restriction")
        )
        check_stock = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("sale_stock_restrict.check_stock")
        )
        if product_restriction:
            if check_stock == "on_hand_quantity":
                self.qty_available = self.product_id.qty_available
            if check_stock == "forecast_quantity":
                self.forecast_quantity = self.product_id.virtual_available


class SaleOrder(models.Model):
    """Class to add fields in sale order and a function for confirming
    quotation."""

    _inherit = "sale.order"

    def action_confirm(self):
        """Restrict confirming a quotation if the product is out of stock."""
        onhand_check = False
        forecast_check = False
        low_qty = ["Can't confirm the sale order due to: \n"]
        for rec in self.order_line:
            product_restriction = tools.str2bool(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("sale_stock_restrict.product_restriction")
            )
            check_stock = (
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("sale_stock_restrict.check_stock")
            )
            if (
                product_restriction
                and not self.website_id
                and rec.product_id.type == "consu"
            ):
                if (
                    check_stock == "on_hand_quantity"
                    and rec.product_uom_qty > rec.qty_available
                ):
                    onhand_check = True
                    low_qty.append(
                        f"You have added {rec.product_uom_qty} units of "
                        f"{rec.product_id.name}, but you only have "
                        f"{rec.qty_available} units available."
                    )
                if (
                    check_stock == "forecast_quantity"
                    and rec.product_uom_qty > rec.forecast_quantity
                ):
                    forecast_check = True
                    low_qty.append(
                        f"You have added {rec.product_uom_qty} units of "
                        f"{rec.product_id.name}, but you only have "
                        f"{rec.forecast_quantity} units available."
                    )
        message = " ".join(map(str, low_qty))
        if onhand_check:
            raise ValidationError(message)
        if forecast_check:
            raise ValidationError(message)
        res = super().action_confirm()
        return res

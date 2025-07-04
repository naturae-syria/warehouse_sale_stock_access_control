# -*- coding: utf-8 -*-
"""Restrict confirming sale orders when stock is insufficient."""

from odoo import _, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        """Check stock before confirming when restriction enabled."""
        icp = self.env["ir.config_parameter"].sudo()
        restrict = icp.get_param("sale_stock_restrict.product_restriction", default="False")
        if restrict and restrict not in [False, "False", 0, "0"]:
            check_type = icp.get_param(
                "sale_stock_restrict.check_stock", default="on_hand_quantity"
            )
            for order in self:
                product_quantities = {}
                for line in order.order_line.filtered(lambda l: l.product_id.type == "product"):
                    qty = product_quantities.get(line.product_id, 0) + line.product_uom_qty
                    product_quantities[line.product_id] = qty
                for product, qty_needed in product_quantities.items():
                    available = (
                        product.qty_available
                        if check_type == "on_hand_quantity"
                        else product.virtual_available
                    )
                    if available < qty_needed:
                        raise ValidationError(
                            _("Not enough quantity for %s") % product.display_name
                        )
        return super().action_confirm()

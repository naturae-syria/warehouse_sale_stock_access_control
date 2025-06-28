from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestRestrictModules(TransactionCase):
    def test_sale_stock_restrict_installed(self):
        module = self.env["ir.module.module"].search(
            [("name", "=", "sale_stock_restrict")], limit=1
        )
        self.assertEqual(module.state, "installed")

    def test_stock_product_restriction(self):
        """Confirming an order with insufficient stockable product should fail."""
        self.env["ir.config_parameter"].sudo().set_param(
            "sale_stock_restrict.product_restriction", True
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "sale_stock_restrict.check_stock", "on_hand_quantity"
        )

        product = self.env["product.product"].create(
            {
                "name": "Restricted Product",
                "type": "product",
                "list_price": 10.0,
            }
        )

        partner = self.env.ref("base.res_partner_3")

        order = self.env["sale.order"].create(
            {
                "partner_id": partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": product.id,
                            "product_uom_qty": 1,
                            "name": product.name,
                            "price_unit": product.list_price,
                        },
                    )
                ],
            }
        )

        with self.assertRaises(ValidationError):
            order.action_confirm()

    def test_user_access_restrict_installed(self):
        module = self.env["ir.module.module"].search(
            [("name", "=", "user_access_restrict")], limit=1
        )
        self.assertEqual(module.state, "installed")

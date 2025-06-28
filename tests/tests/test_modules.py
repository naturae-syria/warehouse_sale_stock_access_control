from odoo.tests.common import TransactionCase


class TestRestrictModules(TransactionCase):
    def test_sale_stock_restrict_installed(self):
        module = self.env["ir.module.module"].search(
            [("name", "=", "sale_stock_restrict")], limit=1
        )
        self.assertEqual(module.state, "installed")

    def test_user_access_restrict_installed(self):
        module = self.env["ir.module.module"].search(
            [("name", "=", "user_access_restrict")], limit=1
        )
        self.assertEqual(module.state, "installed")

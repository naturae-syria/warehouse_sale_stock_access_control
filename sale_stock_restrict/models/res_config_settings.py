# -*- coding: utf-8 -*-
"""Configuration parameters for sale stock restriction."""

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Extend settings with stock restriction options."""

    _inherit = "res.config.settings"

    product_restriction = fields.Boolean(
        string="Restrict Sale Order Confirmation",
        config_parameter="sale_stock_restrict.product_restriction",
    )
    check_stock = fields.Selection(
        [
            ("on_hand_quantity", "On Hand Quantity"),
            ("forecast_quantity", "Forecast Quantity"),
        ],
        default="on_hand_quantity",
        config_parameter="sale_stock_restrict.check_stock",
        string="Quantity Check Type",
    )

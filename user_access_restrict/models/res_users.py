# -*- coding: utf-8 -*-
###############################################################################
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
###############################################################################
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    """Extend res.users with custom access type and allowed warehouses."""

    _inherit = "res.users"

    access_type = fields.Selection(
        [
            ("custom_manager", "مدير مخصص"),
            ("custom_user", "مستخدم مخصص"),
        ],
        string="نوع الوصول",
    )
    allowed_warehouse_ids = fields.Many2many(
        "stock.warehouse", string="المستودعات المصرح بها"
    )

    @api.constrains("access_type", "allowed_warehouse_ids")
    def _check_allowed_warehouses(self):
        """Ensure at least one warehouse is set when access type defined."""
        for user in self:
            if user.access_type and not user.allowed_warehouse_ids:
                raise ValidationError("يجب تحديد مستودع واحد على الأقل")

    def write(self, vals):
        """Ensure group assignment follows access type."""
        res = super().write(vals)
        if "access_type" in vals:
            for user in self:
                user._update_groups()
        return res

    def create(self, vals_list):
        users = super().create(vals_list)
        users._update_groups()
        return users

    def _update_groups(self):
        """Assign groups based on access type."""
        group_manager = self.env.ref(
            "user_access_restrict.group_user_access_custom_manager",
            raise_if_not_found=False,
        )
        group_user = self.env.ref(
            "user_access_restrict.group_user_access_custom_user",
            raise_if_not_found=False,
        )
        for user in self:
            if group_manager and group_user:
                if user.access_type == "custom_manager":
                    user.write(
                        {"groups_id": [(3, group_user.id), (4, group_manager.id)]}
                    )
                elif user.access_type == "custom_user":
                    user.write(
                        {"groups_id": [(3, group_manager.id), (4, group_user.id)]}
                    )
                else:
                    user.write(
                        {"groups_id": [(3, group_manager.id), (3, group_user.id)]}
                    )


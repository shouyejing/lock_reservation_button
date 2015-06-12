from openerp import models, fields, api, exceptions, _


class Picking(models.Model):
    _inherit = 'stock.picking'

    @api.one
    def _compute_is_current_user_admin(self):
        self.is_current_user_admin = self.env.ref("base.group_system") in self.env.user.groups_id

    is_current_user_admin = fields.Boolean(compute=_compute_is_current_user_admin, readonly=True)
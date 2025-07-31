from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    social_network_ids = fields.One2many(
        'partner.social.network',
        'partner_id',
        string='Redes Sociales'
    )
    profile_complete = fields.Boolean('Perfil completo', compute='_compute_profile_complete', store=True)

    @api.depends('social_network_ids')
    def _compute_profile_complete(self):
        for partner in self:
            partner.profile_complete = False
            if partner.social_network_ids.mapped('social_network_id.type') == ['facebook', 'linkedin', 'instagram']:
                partner.profile_complete = True

    # def get_social_accounts(self):
    #     return {
    #         'facebook': self.facebook_url,
    #         'linkedin': self.linkedin_url,
    #         'instagram': self.instagram_url,
    #         'complete': self.profile_complete,
    #     }

    def show_profile_complete(self):
        """Method to check if the partner's profile is complete."""
        return self.profile_complete
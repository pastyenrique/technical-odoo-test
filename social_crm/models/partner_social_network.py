from odoo import fields, models, api


class PartnerSocialNetwork(models.Model):
    _name = 'partner.social.network'
    _description = 'Redes Sociales del Partner'

    partner_id = fields.Many2one('res.partner', string='Contacto')
    social_network_id = fields.Many2one(
        'social.network',
        string='Red Social',
        required=True
    )
    url = fields.Char(string='URL', required=True)
    name = fields.Char(related='social_network_id.name', string='Nombre', readonly=True)
    media_type = fields.Selection(related='social_network_id.type', string='Tipo', readonly=True)
    image = fields.Binary(related='social_network_id.image', string='Imagen', readonly=True)

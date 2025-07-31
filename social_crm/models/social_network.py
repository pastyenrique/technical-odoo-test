from odoo import fields, models, api


class SocialNetwork(models.Model):
    _name = 'social.network'

    name = fields.Char("Nombre Red Social", required=True)
    type = fields.Selection([
        ('facebook', 'Facebook'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('other', 'Other')
    ], string="Tipo Red Social", required=True)
    image = fields.Binary("Icono Red Social", required=True)
    partner_id = fields.Many2one('res.partner', string="User", ondelete='cascade')

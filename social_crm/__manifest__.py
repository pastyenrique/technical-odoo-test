{
    'name': 'CRM Social Media Integration',
    'version': '13.0.1.0.0',
    'category': 'CRM',
    'summary': 'Integración de redes sociales en CRM',
    'description': """
        Extensión del módulo CRM para registrar y mostrar redes sociales de clientes.
        Incluye filtros y página web para promoción de clientes.
    """,
    'author': 'Pastor Enrique Sánchez',
    'depends': ['crm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/website_templates.xml',
        'views/assets.xml',
        'views/social_network_views.xml',
        'views/menu.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
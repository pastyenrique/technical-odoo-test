from odoo import http
from odoo.http import request


class WebsiteClients(http.Controller):

    @http.route(['/page/clients', '/page/clients/page/<int:page>'], type='http', auth="public", website=True)
    def clients_page(self, page=1, search='', **kw):
        Partner = request.env['res.partner']
        domain = []

        if search:
            domain += ['|', ('name', 'ilike', search), ('social_network_ids.url', 'ilike', search)]

        total = Partner.search_count(domain)
        pager = request.website.pager(
            url='/page/clients',
            total=total,
            page=page,
            step=12
        )

        partners = Partner.search(domain, limit=12, offset=pager['offset'])

        return request.render("social_crm.clients_page", {
            'partners': partners,
            'pager': pager,
            'search': search,
        })
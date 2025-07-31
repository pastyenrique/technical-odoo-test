from . import models
from . import tests

# def pre_init_check(cr):
#     from odoo.service import common
#     from odoo.exceptions import Warning
#     version_info = common.exp_version()
#     server_series = version_info.get('server_series')
#     if server_series != '13.0':
#         raise Warning('Module support Odoo series 13.0 found {}.'.format(server_series))
#     return True

# -*- coding: utf-8 -*-
# from odoo import http


# class ResCompany(http.Controller):
#     @http.route('/res_company/res_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_company/res_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_company.listing', {
#             'root': '/res_company/res_company',
#             'objects': http.request.env['res_company.res_company'].search([]),
#         })

#     @http.route('/res_company/res_company/objects/<model("res_company.res_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_company.object', {
#             'object': obj
#         })

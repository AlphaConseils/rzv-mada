# -*- coding: utf-8 -*-
# from odoo import http


# class RzvBase(http.Controller):
#     @http.route('/rzv_base/rzv_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_base/rzv_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_base.listing', {
#             'root': '/rzv_base/rzv_base',
#             'objects': http.request.env['rzv_base.rzv_base'].search([]),
#         })

#     @http.route('/rzv_base/rzv_base/objects/<model("rzv_base.rzv_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_base.object', {
#             'object': obj
#         })

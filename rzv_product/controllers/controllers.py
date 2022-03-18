# -*- coding: utf-8 -*-
# from odoo import http


# class RzvProduct(http.Controller):
#     @http.route('/rzv_product/rzv_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_product/rzv_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_product.listing', {
#             'root': '/rzv_product/rzv_product',
#             'objects': http.request.env['rzv_product.rzv_product'].search([]),
#         })

#     @http.route('/rzv_product/rzv_product/objects/<model("rzv_product.rzv_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_product.object', {
#             'object': obj
#         })

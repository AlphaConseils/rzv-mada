# -*- coding: utf-8 -*-
# from odoo import http


# class RzvStock(http.Controller):
#     @http.route('/rzv_stock/rzv_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_stock/rzv_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_stock.listing', {
#             'root': '/rzv_stock/rzv_stock',
#             'objects': http.request.env['rzv_stock.rzv_stock'].search([]),
#         })

#     @http.route('/rzv_stock/rzv_stock/objects/<model("rzv_stock.rzv_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_stock.object', {
#             'object': obj
#         })

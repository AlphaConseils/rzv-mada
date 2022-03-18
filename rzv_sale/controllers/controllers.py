# -*- coding: utf-8 -*-
# from odoo import http


# class RzvSale(http.Controller):
#     @http.route('/rzv_sale/rzv_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_sale/rzv_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_sale.listing', {
#             'root': '/rzv_sale/rzv_sale',
#             'objects': http.request.env['rzv_sale.rzv_sale'].search([]),
#         })

#     @http.route('/rzv_sale/rzv_sale/objects/<model("rzv_sale.rzv_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_sale.object', {
#             'object': obj
#         })

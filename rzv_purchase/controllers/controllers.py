# -*- coding: utf-8 -*-
# from odoo import http


# class RzvPurchase(http.Controller):
#     @http.route('/rzv_purchase/rzv_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_purchase/rzv_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_purchase.listing', {
#             'root': '/rzv_purchase/rzv_purchase',
#             'objects': http.request.env['rzv_purchase.rzv_purchase'].search([]),
#         })

#     @http.route('/rzv_purchase/rzv_purchase/objects/<model("rzv_purchase.rzv_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_purchase.object', {
#             'object': obj
#         })

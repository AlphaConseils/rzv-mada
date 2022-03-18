# -*- coding: utf-8 -*-
# from odoo import http


# class RzvInvoice(http.Controller):
#     @http.route('/rzv_invoice/rzv_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_invoice/rzv_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_invoice.listing', {
#             'root': '/rzv_invoice/rzv_invoice',
#             'objects': http.request.env['rzv_invoice.rzv_invoice'].search([]),
#         })

#     @http.route('/rzv_invoice/rzv_invoice/objects/<model("rzv_invoice.rzv_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_invoice.object', {
#             'object': obj
#         })

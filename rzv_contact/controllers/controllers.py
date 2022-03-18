# -*- coding: utf-8 -*-
# from odoo import http


# class RzvContact(http.Controller):
#     @http.route('/rzv_contact/rzv_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rzv_contact/rzv_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rzv_contact.listing', {
#             'root': '/rzv_contact/rzv_contact',
#             'objects': http.request.env['rzv_contact.rzv_contact'].search([]),
#         })

#     @http.route('/rzv_contact/rzv_contact/objects/<model("rzv_contact.rzv_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rzv_contact.object', {
#             'object': obj
#         })

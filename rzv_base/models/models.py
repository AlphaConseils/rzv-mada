# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rzv_base(models.Model):
#     _name = 'rzv_base.rzv_base'
#     _description = 'rzv_base.rzv_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

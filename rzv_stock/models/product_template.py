# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Product_template(models.Model):
    _inherit='product.template'

    brand = fields.Char(
        string='Brand',
        required=False)
    
    pcb = fields.Float(
        string='PCB',
        required=False)
    sub_pcb = fields.Float(
        string='Sub-PCB',
        required=False)
    unit_per_box = fields.Float(
        string='Nb unit/box',
        required=False)
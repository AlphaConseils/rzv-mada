# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stock_quant(models.Model):
    _inherit="stock.quant"

    box_per_product = fields.Float('Nbr d unité par carton', compute='_get_number_product_per_box')
    box=fields.Float('Box', compute='_box_management')
    
    @api.depends('inventory_quantity')
    def _get_number_product_per_box(self):
        get_box=self.product_tmpl_id.unit_per_box
        self.box_per_product=get_box

    @api.depends('inventory_quantity')
    def _box_management(self):
        bm=self.inventory_quantity_auto_apply/self.box_per_product
        self.box=bm
    
    # product_id = fields.Many2one('res.partner, string='Partner', related='order_id.partner_id')
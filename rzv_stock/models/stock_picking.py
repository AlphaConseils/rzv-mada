# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stock_picking(models.Model):
    _inherit="stock.picking"
    transporter = fields.Char('Transporteur')
    
    def get_prod_id(self,p_id):
        return p_id.default_code
        get_id=0
        # isinstance(5, int)
        # if isinstance(p_id,str):
        # emp_str = ""
        # for m in p_id:
        #     if m.isdigit():
        #         emp_str = emp_str + m
        # get_id=int(emp_str)
        
        # product=self.env['product.product'].search([
        # ('id', '=', get_id)
        # ])
        # ref=product.product_tmpl_id.default_code
        # return ref
            
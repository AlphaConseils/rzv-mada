# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sale_order(models.Model):
    _inherit='sale.order'

    percentage_commission = fields.Float(
        string='Percentage',
        required=False)
    commission = fields.Float(compute='_compute_total')

    @api.depends('percentage_commission', 'amount_total')
    def _compute_total(self):
        for record in self:
            record.commission=(record.amount_total * record.percentage_commission)/100
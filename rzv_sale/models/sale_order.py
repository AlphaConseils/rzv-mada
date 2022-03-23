# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sale_order(models.Model):
    _inherit='sale.order'

    percentage_commission = fields.Float(
        string='Percentage',compute='_compute_get_commission',
        required=False)
    commission = fields.Monetary(compute='_compute_total',)

    @api.depends('amount_total')
    def _compute_get_commission(self):
        # import pudb; pudb.set_trace()

        search_user_id=self.user_id
        employee_comm=self.env['hr.employee'].search(
            [
                ("user_id", "=",search_user_id.id ),
            ]
        )
        print(employee_comm)
        self.percentage_commission=employee_comm.percentage_commission

    @api.depends('percentage_commission', 'amount_total')
    def _compute_total(self):
        for record in self:
            

            comm=record.percentage_commission
            record.commission=(record.amount_total * comm)/100

class Hr_employee(models.Model):
    _inherit='hr.employee'

    percentage_commission = fields.Float('Percentage commission')
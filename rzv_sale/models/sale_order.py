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
    
    def convert_date(self,date_order):
        import datetime
        months = ["Unknown",
                  "Janvier",
                  "Février",
                  "Mars",
                  "Avril",
                  "Mai",
                  "Juin",
                  "Juillet",
                  "Aout",
                  "Septembre",
                  "Octobre",
                  "Novembre",
                  "Décembre"]

        d_date = date_order
        date = d_date.strftime("%d")
        month = (months[d_date.month])
        year = d_date.strftime("%Y")
        days = ["Lundi", "Mardi", "Mercredi",
                "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        wd = datetime.datetime.today().weekday()
        weekday = days[wd] + " " + date+" " + month + " " + year
        return weekday


    def num_to_word(self,number):
        from num2words import num2words
        pre = float(number)
        text = ''
        entire_num = int((str(pre).split('.'))[0])
        decimal_num = int((str(pre).split('.'))[1])
        if decimal_num < 10:
            decimal_num = decimal_num * 10        
        text+=num2words(entire_num, lang='fr')
        text+=' et '
        text+=num2words(decimal_num, lang='fr')
        return text
class Hr_employee(models.Model):
    _inherit='hr.employee'

    percentage_commission = fields.Float('Percentage commission')
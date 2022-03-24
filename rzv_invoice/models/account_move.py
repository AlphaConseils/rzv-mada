# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Account_move(models.Model):
    _inherit='account.move'
    
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

    def get_echeance_nd(self,origin):
        # import pudb; pudb.set_trace()
        
        origin_invoice=self.env['sale.order'].search([
                            ('name', '=', origin)],)
        return origin_invoice.payment_term_id.name

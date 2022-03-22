from odoo import models, fields, api
class Company(models.Model):
    _inherit="res.company"

    cif = fields.Char("CIF", company_dependent=True)
    nif=fields.Char("NIF",company_dependent=True)
    stat=fields.Char("STAT",company_dependent=True)

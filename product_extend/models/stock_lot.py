# -*- encoding: utf-8 -*-

from odoo import models,fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'stock.production.lot'

    final_adress = fields.Char(string=u'Adresse Client Final')

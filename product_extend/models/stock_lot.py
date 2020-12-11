# -*- encoding: utf-8 -*-

from odoo import models,fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'stock.production.lot'

    final_adress = fields.Char(string=u'Adresse Client Final')


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.constrains('default_code')
    def _check_description(self):
        product_ids = self.search([['default_code', '=', self.default_code], ['id', '!=', self.id]])
        if product_ids:
            raise ValidationError(u"Le code doit être unique")

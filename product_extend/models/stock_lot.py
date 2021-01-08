# -*- encoding: utf-8 -*-

from odoo import models,fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'stock.production.lot'

    final_adress = fields.Char(string=u'Lieu d\'instalation')
    date_installation = fields.Date(string=u'Date d\'instalation')
    type_produit = fields.Many2one('product.category', related='product_id.categ_id', string=u'Type d\'article')
    s_n = fields.Char('S/N')
    generation = fields.Char('Génération')
    version_cartes = fields.Char('Version de cartes')
    client = fields.Many2one('res.partner', 'Client')
    client_final = fields.Many2one('res.partner', 'Client final')
    commentaire = fields.Text('Commentaire')


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.constrains('default_code')
    def _check_description(self):
        product_ids = self.search([['default_code', '=', self.default_code], ['id', '!=', self.id]])
        if product_ids:
            raise ValidationError(u"Le code doit être unique")

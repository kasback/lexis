# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    num_decompte = fields.Char('Numéro du Décompte Provisoire')
    ref_client = fields.Char('Réference Client')
    objet = fields.Char('Objet')
    texte_en_tete = fields.Text("Texte de l'en-tête")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    poste = fields.Integer('Poste', compute='_compute_next_poste')

    @api.depends('order_id.order_line')
    def _compute_next_poste(self):
        for index, rec in enumerate(self):
            rec.poste = index + 1

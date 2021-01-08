# -*- coding: utf-8 -*-

from odoo import models, fields, api

REVISIONS = [
    (0, 'Révision A'),
    (1, 'Révision B'),
    (2, 'Révision C'),
    (3, 'Révision D'),
    (4, 'Révision E'),
    (5, 'Révision F'),
    (6, 'Révision G'),
    (7, 'Révision H'),
    (8, 'Révision I'),
    (9, 'Révision J'),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    num_decompte = fields.Char('Numéro du Décompte Provisoire')
    ref_client = fields.Char('Réference Client')
    objet = fields.Char('Objet')
    texte_en_tete = fields.Text("Texte de l'en-tête")
    revision = fields.Char('Révision', default='Révision A')
    revision_index = fields.Integer('Révision Index', default=0)

    def write(self, vals):
        if vals.get('order_line', None):
            vals['revision_index'] = self.revision_index + 1
            vals['revision'] = REVISIONS[vals['revision_index']][1]
        res = super(SaleOrder, self).write(vals)
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    poste = fields.Integer('Poste', compute='_compute_next_poste', default=False)

    @api.depends('order_id.order_line')
    def _compute_next_poste(self):
        for index, rec in enumerate(self):
            rec.poste = index + 1

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    num_decompte = fields.Char('Numéro du Décompte Provisoire')
    ref_client = fields.Char('Réference Client')
    condition_paiement = fields.Char('Condition / Paiement')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    marche_item = fields.Char(string='item')

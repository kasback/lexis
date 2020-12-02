# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'sale.order'

    num_decompte = fields.Char('Numéro du Décompte Provisoire')
    ref_client = fields.Char('Réference Client')
    objet = fields.Char('Objet')
    texte_en_tete = fields.Text("Texte de l'en-tête")

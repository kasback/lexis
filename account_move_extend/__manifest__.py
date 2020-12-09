# -*- coding: utf-8 -*-

{
    'name': u'Lexises -- Impression des Documents commerciaux',
    'version': '1.0',
    'summary': u'',
    'category': 'Gestion Commerciale',
    'author': 'Osisoftware',
    'website': '',
    'depends': [
        'base', 'web', 'account', 'partner_extend'
    ],
    'data': [
        'report/report_templates.xml',
        'report/report_invoice.xml',
        'report/report.xml',
        'views/account_move_views.xml',
        # 'report/report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

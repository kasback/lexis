# -*- coding: utf-8 -*-

{
    'name': u'Lexises -- Impression des Documents commerciaux',
    'version': '1.0',
    'summary': u'',
    'category': 'Gestion Commerciale',
    'author': 'Osisoftware',
    'website': '',
    'depends': [
        'base', 'web', 'sale'
    ],
    'data': [
        'report/report_sale.xml',
        'report/report.xml',
        'views/sale_order_views.xml',
        # 'report/report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

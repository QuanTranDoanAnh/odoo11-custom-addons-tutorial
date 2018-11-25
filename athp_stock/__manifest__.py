# -*- coding: utf-8 -*-
{
    'name': "ATHP Stock Management",

    'summary': """
        Addons to support stock management processes at Hoa Phat""",

    'description': """
        Addons to support stock management processes at Hoa Phat
    """,

    'author': "BLD Co., Ltd.,",
    'website': "http://www.bld.com.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.1',
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/athp_stock_product_views.xml',
        'views/athp_stock_views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
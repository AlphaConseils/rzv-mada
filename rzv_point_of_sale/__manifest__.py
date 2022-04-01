# -*- coding: utf-8 -*-
{
    'name': "rzv_point_of_sale",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','rzv_base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security_pos.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],'license': 'LGPL-3',
    'assets': {
        # 'point_of_sale.assets': [
        #     'custom_pos_receipt/static/src/js/pos_model.js',
        # ],
        'web.assets_qweb': [
            "rzv_point_of_sale/static/src/xml/custom_print.xml",
            "rzv_point_of_sale/static/src/xml/custom_point_of_sale.xml",
        ],
    },
}

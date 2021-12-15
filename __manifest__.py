# -*- coding: utf-8 -*-
{
    'name': "task_app",

    'summary': """
        Application for managing different tasks""",

    'description': """
        In this application you can add different tasks to do it
        Also you can modify diffent things!
    """,

    'author': "Alberto Aparicio",
    'website': "http://www.aaparicio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/task_view.xml',
        'views/category_view.xml',        
        'views/menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    'name': "dimensions_14",

    'summary': """
        Dimensions""",

    'description': """
        Dimensions
    """,

    'author': "Prixgen Tech Solutions Pvt. Ltd.",
    'company': "Prixgen Tech Solutions Pvt. Ltd.",
    'website': "https://www.prixgen.com",

    'category': 'Customization',
    'version': '14.0.3.4',

    'depends': ['base','account','hr_expense'],

    'data': [
        'security/ir.model.access.csv',
        'views/dimension.xml',
        'views/account.xml',
        'views/budget.xml',
        'views/hr.xml'
    ],
}

# -*- coding: utf-8 -*-
{
    "name": "Sales Quotation Template WOO",
    "version": "14.0.0.20",
    'author': 'Prixgen Tech Solutions Pvt. Ltd.',
    'company': 'Prixgen Tech Solutions Pvt. Ltd.',
    'website': 'https://www.prixgen.com',
    "summary": """
    """,
    "description": """
    """,
    "category": "Sales",
    "depends": [
        'sale_management','base',
    ],
    "data": [
        'security/ir.model.access.csv',
        #Templates
        'templates/custom_header_footer.xml',
        'templates/pro_forma_custom_header.xml',
        'templates/sales_order_custom_header.xml',
        'templates/quotation_export.xml',
        'templates/sale_export.xml',
        'templates/pro_forma_export.xml',
        #Templates

        #*****************************************************************************#

        #Pro-Forma Reports
        'views/pro_forma_reports/pf_inovice_wo_tax.xml',
        'views/pro_forma_reports/pf_invoice_with_tax.xml',
        'views/pro_forma_reports/pf_invoice_export.xml',
        #Pro-Forma Reports

        #*****************************************************************************#

        #Sale Quotation Reports
        'views/sale_quotation_reports/sales_quotation_template.xml',
        'views/sale_quotation_reports/sale_quotation_template_with_tax.xml',
        'views/sale_quotation_reports/sale_quotation_export.xml',
        'views/sale_quotation_reports/sale_quotation_export_wo_dis.xml',
        'views/sale_quotation_reports/sale_quotation_template_with_tax_wo_disc.xml',
        
        #Sale Quotation Reports

        #*****************************************************************************#
        
        #Sale Order Reports
        'views/sale_order_reports/so_wo.xml',
        'views/sale_order_reports/so_with.xml',
        'views/sale_order_reports/so_export.xml',
        #Sale Order Reports

        #*****************************************************************************#

        #New Fields
        'views/new_fields/sale_order.xml',
        
        #New Fields

        #*****************************************************************************#

        #Custom Menu
        'menus/port_menu.xml',
        
        #New Fields

        #*****************************************************************************#

        #*****************************************************************************#

        #Wizards
        'wizard/sale_order_print_wiz.xml',
        
        #New Fields

        #*****************************************************************************#
       
    ],
    "installable": True,
    "auto_install": False,
}

# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2023 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    "name": "Purchase Report Extended",
    "license": "Other proprietary",
    "author": "Uncanny Consulting Services LLP",
    "website": "https://uncannycs.com",
    "category": "Inventory/Purchase",
    "summary": "Purchase Report Extended",
    "description": """Purchase Report Extended""",
    "version": "18.1",
    "depends": ["base","web", "purchase","purchase_stock"],
    "data": [
        "views/res_company_views.xml",
        'views/purchase_order_report.xml',
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
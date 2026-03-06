{
    'name': 'Sales Customization',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'practice on Sales Customization',
    'description': 'Trying demo',
    'author': 'Parth',
    'category': 'Education',
    'depends': ['base','sale','contacts'],
    'data': [
    # 'security/ir.model.access.csv',
    'views/account_move_view.xml',  
    "views/product_template_view.xml", 
    'views/purchase_order_view.xml',
    "views/res_partner_view.xml",
    'views/sale_line_view.xml',
    'views/sale_order_view.xml',
    'views/stock_picking_view.xml',
],

    'application': True,
    'installable': True,
    'auto_install': False,
}

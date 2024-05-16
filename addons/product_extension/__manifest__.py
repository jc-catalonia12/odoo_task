{
    'name': 'Product Extension',
    'summary': 'Addon to extend product functionalities',
    'description': 'Add additional fields to the product template form view.',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}

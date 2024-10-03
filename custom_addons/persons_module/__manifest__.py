
{
    'name': 'Persons',
    'category': 'Website',
    'sequence': -100,
    'summary': 'Module for managing persons',
    'version': '1.0',
    'depends': ["base", 'website'],
    'data': [
        'security/ir.model.access.csv'
        'views/persons_views.xml',
        'views/persons_template.xml',
        'views/persons_form_template.xml',

    ],
    'installable': True,
    'demo': [],
    'application': True,
}
{
    'name': 'College ERP',
    'version': '1.2',
    'category': 'Education',
    'summary': 'College ERP to store records ',
    'author': 'Parth Barot',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/college_department_views.xml',
        'views/college_subject_views.xml',
        'views/college_student_views.xml',
        'views/college_menu.xml'
    ],
    'application': True,
    'installable': True
}       

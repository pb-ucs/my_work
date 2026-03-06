from odoo import models, fields

class CollegeDepartment(models.Model):
    _name = 'orm.department'
    _description = 'College Department'

    name = fields.Char(required=True)
    hod = fields.Char(string='HOD Name')

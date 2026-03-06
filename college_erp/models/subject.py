from odoo import models, fields

class CollegeSubject(models.Model):
    _name = 'college.subject'
    _description = 'College Subject'

    name = fields.Char(required=True)
    code = fields.Char(string='Subject Code')


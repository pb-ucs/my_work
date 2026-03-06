from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'

    name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name")
    # email = fields.Char()
    email = fields.Char(copy=False)
    dob = fields.Date(string='DOB')
    cgpa = fields.Float()


    department_id = fields.Many2one(
        'college.department',
        string='Department'
    )

    subject_ids = fields.Many2many(
        'college.subject',
        string='Subjects'
    )

    fees_paid = fields.Boolean()

    mark_ids = fields.One2many(
        'college.student.mark',
        'student_id',
    )

    # full_name = fields.Char(
    #     string='Full Name',
    #     # compute='_compute_full_name',
    #     store=True
    # )

    # age = fields.Integer(
    #     string='Age',
    #     compute='_compute_age',
    #     store=True
    # )
# -----------------------------------------------------------------------------------------------
# Decorators

#     @api.depends('name', 'l_name')
#     def _compute_full_name(self):
#         for record in self:
#             record.full_name = f"{record.name} {record.l_name}"

#     @api.onchange('department_id')
#     def _onchange_department(self):
#         if self.department_id:
#             return {
#                 'warning': {
#                     'title': "Department Changed",
#                     'message': "Please re-check subjects after changing department."
#                 }
#             }

#     @api.constrains('age')
#     def _check_age(self):                 
#      for rec in self:
#          if rec.age < 16:
#              raise ValidationError("Minimum age is 16")

#     ##@api.model
#     ##def create(self, vals):
#     ##    if not vals.get('name'):
#     ##        raise ValidationError("enter a name")    # IT WONT WORK AS IT CALLS ONLY VAL_LIST
#     ##    else:
#     ##        return super(CollegeStudent, self).create(vals)

#     @api.model_create_multi
#     def create(self, vals_list):
#         for vals in vals_list:
#             name = vals.get('name')
#             name = vals.get('l_name')
#             if not name:
#                 raise ValidationError("Student name cannot be empty")
#             age = vals.get('age')
#             if  age < 16:
#                 raise ValidationError("Minimum age is 16")
#         return super(CollegeStudent, self).create(vals_list)

#     @api.depends_context('show_last_name_first') 
#     def _compute_full_name(self):
#         for record in self:
#             first = record.name
#             last = record.l_name or ''
#             if self.env.context.get('show_last_name_first'):
#                 record.full_name = f"{last}, {first}"
#             else:
#                 record.full_name = f"{first} {last}"

# # Task given by smit bhai
#     @api.depends('dob')
#     def _compute_age(self):
#         days_in_year = 365.2425
#         today = date.today()
#         for rec in self:
#             if rec.dob >= today:
#                  raise ValidationError(
#                     "Date of Birth cannot be today or a future date."
#                 )
#             elif rec.dob:
#                 rec.age = int((today - rec.dob).days / days_in_year)
#             else:
#                 rec.age = 0

# ---------------------------------------------------------------------------------------------------------
# ORM
    # @api.model_create_multi 
    # def create(self,vals_list):
    #     print("vals_list:", vals_list)
    #     print("type(vals_list):", type(vals_list))        # print('self',self)
        # rtn =zyy
        # rtn = super(CollegeStudent,self).create(vals_list) 
        # print(rtn)    

    # @api.model_create_multi          # by vraj bhai
    # def addfield(self,):
    # # print('self',self)
    # self.create(vals) 
    # print(rtn)

    @api.model_create_multi
    def create(self,vals_list):                               # its working but not printing prints in terminal(in for loop)
        print('create method called')
        print('vals before create', vals_list)
        return super(CollegeStudent,self).create(vals_list) 


    def write(self,vals):
        print(self)                                     # print current id
        print(vals)                                     # print changes made in dict
        rtn = super(CollegeStudent,self).write(vals) 
        print(rtn)                                      # print true if changes made successfully
        return rtn

    def duplicate_rec(self):
        print(self) 
        duplicate = self.copy() 
        print(duplicate)

    # def delete_exist_rec(self):
    #     print('unlink method called')
    #     print(self)
    #     recoed = self.env['college.student'].browse([111])
    #     if not CollegeStudent.exists():
    #         print('Record isnt present in batabase')
    #     else:
    #         rtn = super(CollegeStudent,self).unlink() 
    #     print(rtn)
    #     return rtn

    def delete_rec(self):
        print('unlink method called')
        print(self)
        rtn = super(CollegeStudent,self).unlink() 
        print(rtn)
        return rtn

    def custom_search(self):
        # print (self.search([]))
        # print (self.search([],limit=10,offset=3,order='name'))

        print('custom method clicked')
        print(self)
        print (self.env['college.student'].search([]))
        total_rec = self.env['college.student'].search_count([])
        print(total_rec) 

    # def read_data(self):
    #     print('read method clicked')
    #     print(self)
    #     # print(self.read())                                # it will give all data from db
    #     print(self.env['college.student'].read())           # it will give only record id








# -----------------------------------------------------------------------------------------------------------
class CollegeStudentMark(models.Model):
    _name = 'college.student.mark'
    _description = 'Student Marks'

    student_id = fields.Many2one(
        'college.student',
        string='Student',
    )
    subject_id = fields.Many2one(
        'college.subject',
        string='Subject',
    )
    marks = fields.Integer(string='Marks')

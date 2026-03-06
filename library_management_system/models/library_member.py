from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(required=True)
    member_code = fields.Char(string="Member ID")
    # photo = fields.Image()
    dob = fields.Date()
    gender = fields.Selection(
            [('male','Male'),('female','Female'),('other','Other')]
        )
    # gender = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    address = fields.Text()
    about = fields.Char()


    def details (self):
        # action = self.env('library_management_system.action_member_detail').read()[0]
        # return action
        return {
            'type': 'ir.actions.act_window',
            'name': 'Details',
            'res_model': 'member.detail',
            'view_mode': 'form',
            'target': 'new',
        }

    def test (self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'parth',
            'res_model': 'member.test',
            'view_mode': 'form',
            'target': 'new',
        }

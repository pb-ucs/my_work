from odoo import models, fields

class MemberDetail(models.TransientModel):
	_name = 'member.detail'
	_descripton = 'Member Details'

	email_from = fields.Char(string='email from') 
	email_to = fields.Char(string='email to') 
	email_subject = fields.Text(string='email subject') 
   


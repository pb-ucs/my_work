from odoo import models, fields

class MemberDetail(models.TransientModel):
	_name = 'member.test'
	_descripton = 'Member test'

	test1 = fields.Char(string='fav color') 
	test2 = fields.Char(string='fav fruit') 
	test3 = fields.Text(string='fav show') 
   


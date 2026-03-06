from odoo import models, fields

class AccountMove(models.Model):
	_inherit = 'account.move'

	c_email = fields.Char(string='Email',related='partner_id.email',store=True)	
	# email = fields.Char(string='Email')	

	# def _create_invoices(self):
	# 	res=super(SaleOrder,self)._create_invoices()
	# 	mmm
	# 	return res
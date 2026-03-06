from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	address = fields.Char()
	replaced = fields.Char()
	moved = fields.Char()
	test1 = fields.Char()
	test2 = fields.Char()
	test3 = fields.Char()
	test4 = fields.Char()
	test5 = fields.Char()
	test6 = fields.Char()
	test7 = fields.Char()
	test8 = fields.Char()
	test9 = fields.Char()
	test10 = fields.Char()
	demo_replace = fields.Char()
	dragon = fields.Char()
	partner_id = fields.Many2one('res.partner')
	# test = fields.Char(string='Test', related='partner_id.test',readonly=False)
	email = fields.Char(string='Email', related='partner_id.email',readonly=False)
	# email = fields.Char(string='Email')
	# partner_id = fields.Many2one('res.partner')
	# phone = fields.Char(string='Phone',related='partner_id.phone', readonly=False)
	phone = fields.Char(string='Phone')
	purchase = fields.Char(string='Purchase')
	custom_tax_rate = fields.Char()

	@api.onchange('partner_id')
	def onchange_partner(self):
		if self.partner_id:	
			self.phone = self.partner_id.phone

	# @api.model_create_multi
	# def create(self, vals_list):
	# 	aaa
	# 	res=super(PurchaseOrder,self)._action_confirm()
	# 	return res

	# def _action_confirm(self):
	# 	aaa
	# 	res=super(SaleOrder,self)._action_confirm()
	# 	return res

	@api.model_create_multi 
	def default_get(self, fields_list):
		res = super().default_get(fields_list)
		# Fetch tax rate from System Parameters
		tax_rate = self.env['ir.config_parameter'].sudo().get_param('default.tax.rate')
		if tax_rate:
			res['custom_tax_rate'] = float(tax_rate)  # convert string to float
		return res

	
	


	
	

	

		

	

	
	






	
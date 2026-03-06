from odoo import models, fields, api

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	purchase = fields.Char(string='Purchase')
	phone = fields.Char(string='Phone')
	# email = fields.Char(string='Email')

	# @api.model_create_multi
	# def create(self, vals_list):
	# 	aaa
	# 	res=super(PurchaseOrder,self).create()
	# 	return res

	# def create(self):
	# 	aaa
	# 	res=super(PurchaseOrder,self)._action_confirm()
	# 	return res
	
	# def _action_confirm(self,):
	# 	aaa
	# 	res=super(PurchaseOrder,self)._action_confirm()
	# 	return res

	



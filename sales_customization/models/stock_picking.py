from odoo import models, fields,api

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	phone = fields.Char()
	# c_phone = fields.Char(string='Phone', related='partner_id.phone',store=True)
	test2 = fields.Char()
	email = fields.Char()

	# @api.model_create_multi
	# def create(self, vals_list):
	# 	aaa
	# 	res=super(SaleOrder,self)._action_view_delivery()
	# 	return res

	# def create(self, vals_list):
	# 	aaa
	# 	res=super(SaleOrder,self)._action_comfirm()
	# 	return res

	# def create(self, vals_list):
	# 	aaa
	# 	res=super(PurchaseOrder,self).button_comfirm()
	# 	return res

	


	


	

	
		


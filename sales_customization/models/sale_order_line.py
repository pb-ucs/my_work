from odoo import models, fields, api

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	quality = fields.Char()
	category = fields.Char(string='Category')

	# def _prepare_procurement_values(self,group_id):
	# 	vals = super()._prepare_procurement_values(group_id=group_id)
	# 	vals['purchase'] = self.order_id.purchase
	# 	print(vals)
	# 	return vals

	
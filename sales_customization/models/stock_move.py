from odoo import models, fields, api

class StockMove(models.Model):
	_inherit = 'stock.move'

	# partner_id = fields.Many2one('res.partner')
	phone = fields.Char()

	# def _get_new_picking_values(self):
	# 	vals = super(StockMove,self)._get_new_picking_values()
	# 	vals['phone'] = self.partner_id.phone
	# 	return vals

	# def _action_confirm(self):
	# 	aaa
	# 	res=super(SaleOrder,self)._action_confirm()
	# 	return res


	def _get_new_picking_values(self):
		vals = super()._get_new_picking_values()
		sale = self.sale_line_id.order_id
		if sale:
			vals['phone'] = sale.phone
		return vals




	

	
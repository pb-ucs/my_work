from odoo import models, fields, api

class SaleReport(models.Model):
	_inherit = 'sale.report'

	order_reference = field.Char()
	product_id = field.Char()
	partner_id = field.Char()
	product_um_qty = field.Char()
	price_unit = field.Char()
	price_total = field.Char()
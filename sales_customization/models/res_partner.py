from odoo import models,fields

class ResPartner(models.Model):
	_inherit = 'res.partner'

	payment_term = fields.Text(String="payment_term")
	test7 = fields.Char()
	test8 = fields.Char()
	test9 = fields.Char()
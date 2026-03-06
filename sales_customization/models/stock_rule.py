from odoo import models, fields

class StockRule(models.Model):
	_inherit = 'stock.rule'

	phone=fields.Char()
	purchase=fields.Char()

	# def _action_confirm(self):
	# 	aaa
	# 	res=super(StockRule,self)._action_confirm()
	# 	res=super(PurchaseRule,self)._action_confirm()
	# 	return res

	def _prepare_purchase_order(self, company_id, origins, values):
	    res = super()._prepare_purchase_order(company_id, origins, values)
	    sale = False
	    for val in values:
	        group = val.get('group_id')
	        
	        if group:
	            sale = self.env['sale.order'].search(
	                [('procurement_group_id', '=', group.id)],
	                limit=1
	            )
	            if sale:
	                break
	    if sale and sale.purchase:
	        res.update({
	            'purchase': sale.purchase
	        })
	    return res

	

	

	



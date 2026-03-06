from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    order_reference = fields.Char(string='order')
    product_id = fields.Char(string='product')
    partner_id = fields.Char(string='customer')
    product_uom_qty = fields.Char(string='quantity')
    price_unit = fields.Char(string='price')
    price_total = fields.Char(string='total')
    order_id = fields.Char(string='order reference')
    # company_id = fields.Char(string='company')
    price_subtotal = fields.Char(string='untaxed')


    # def _compute_sale_report(self):
    #     for rec in self:
    #         reports = self.env['sale.report'].search()
    #         b  = reports.sorted(key= lambda r: r.id)      
    #         rec.sale_report_ids = b

    sale_report_ids = fields.One2many(
        "sale.report",
        string="Last 5 Sales",
        compute="_compute_sale_report",
    )

    purchase_report_ids = fields.One2many(
        "purchase.order.line",
        string="Last 5 purchase",
        compute="_compute_purchase_report",
    )

    def _compute_sale_report(self):
        for rec in self:
            reports = self.env['sale.report'].search(
                [('product_tmpl_id', '=', rec.id)],
                order='date desc',
                limit=5
            )
            rec.sale_report_ids = reports

    def _compute_purchase_report(self):
        for rec in self:
            reports = self.env['purchase.order.line'].search(
                [('product_id.product_tmpl_id', '=', rec.id)],
                order='id desc',
                limit=5
            )
            rec.purchase_report_ids = reports

    

   
    
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    report_image = fields.Binary("Report Image", help="Image to be used in reports.")
    report_street = fields.Char("Street")
    report_street2 = fields.Char("Street 2")
    report_city = fields.Char("City")
    report_state_id = fields.Many2one("res.country.state", "State")
    report_country_id = fields.Many2one("res.country", "Country")
    report_zip = fields.Char("ZIP")
    report_email = fields.Char("Email")
    report_website = fields.Char("Website")
    report_phone = fields.Char("Phone")

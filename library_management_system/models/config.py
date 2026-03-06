from odoo import models, api

class ResConfigSettings(models.Model):
    _inherit = 'my.res.config.settings'

    is_confirm = fields.Boolean(string='custom sale order', config_parameter='library_management_system.is_confirm', default=False)

    def update_system_parameter(self):
        new_value = 10 
        # Use set_param to create or update the parameter
        self.env['ir.config_parameter'].set_param('default.tax.rate', new_value)
        return False

    def get_system_parameter(self):
        # The value retrieved will be a string
        value = self.env['ir.config_parameter'].get_param('your_system_parameter_key') 
        # Convert to the appropriate type if needed
        if value is not None:
            value = int(value) 
        return value



    

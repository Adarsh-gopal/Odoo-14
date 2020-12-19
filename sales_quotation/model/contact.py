from odoo import models, fields

class custom_contact(models.Model):
    
    _inherit = 'res.partner'
    fax = fields.Char(string='Fax')
    port_of_discharge = fields.Many2one('contact.port',string='Port of Dishcarge')
    mode_of_delivery = fields.Many2one('mode.of.delivery',string='Mode Of Delivery')
    

class contact_port(models.Model):
    _name = 'contact.port'
    _description = "Custom Contact Port"
    name = fields.Char(string='Port Name')

class mode_of_delivery(models.Model):
    _name = 'mode.of.delivery'
    _description = "Mode Of Delivery"
    name = fields.Char(string='Mode of Delivery')


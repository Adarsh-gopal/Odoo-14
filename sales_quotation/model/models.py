# -*- coding: utf-8 -*-
from odoo import models, fields
class Companuy(models.Model):
	_inherit = 'res.company'
	footer_custom = fields.Binary()
	payment_instructions = fields.Text(string='Payment Instructions')
	info_msg=fields.Text(string='Computer Message')
	export_general_note=fields.Text(string='Export Footline General')
	export_general_note_quotation=fields.Text(string='Export Footline Quotation')
	showrooms=fields.Text(string='Showrooms')
	instagram=fields.Text(string='Instagram Link')
	facebook=fields.Text(string='Facebook Link')

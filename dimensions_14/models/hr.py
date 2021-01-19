# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrExpense(models.Model):
    _inherit = "hr.expense"

    name_system_filter = fields.Many2many(related='account_id.dimension_name_ids',string="Name Filter")
    dimension_name_id = fields.Many2one('dimension.name', string='Dimension')
    value_system_filter = fields.Many2many(related='dimension_name_id.dimension_value_ids',string="Value Filter")
    dimension_value_id = fields.Many2one('dimension.value')

    @api.onchange('account_id')
    def _onchange_of_ai(self):
        self.dimension_name_id = False

    @api.onchange('dimension_name_id')
    def _onchange_of_dn(self):
        self.dimension_value_id = False
    
    def _get_account_move_line_values(self):
        result = super(HrExpense, self)._get_account_move_line_values()

        for expense in self:
            move_line_values = result.get(expense.id)
            for move_line in move_line_values:
                move_line['dimension_name_id'] = expense.dimension_name_id.id
                move_line['dimension_value_id'] = expense.dimension_value_id.id
        
        return result


# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    dimension_name_id = fields.Many2one('dimension.name', related='move_id.dimension_name_id', store=True)
    dimension_value_id = fields.Many2one('dimension.value', related='move_id.dimension_value_id', store=True)


class BudgetPositionLine(models.Model):
    _name = 'budget.position.line'

    budget_post_id = fields.Many2one('account.budget.post')

    account_id = fields.Many2one('account.account')
    name_system_filter = fields.Many2many(related='account_id.dimension_name_ids',string="Name Filter")
    dimension_name_id = fields.Many2one('dimension.name', string='Dimension')
    value_system_filter = fields.Many2many(related='dimension_name_id.dimension_value_ids',string="Value Filter")
    dimension_value_id = fields.Many2one('dimension.value')


class AccountBudgetPost(models.Model):
    _inherit = 'account.budget.post'

    budget_line_ids = fields.One2many('budget.position.line','budget_post_id')

    @api.onchange('budget_line_ids')
    def _onchange_budget_line_ids(self):
        self.account_ids = [(6, 0, self.budget_line_ids.mapped('account_id').ids)]
    

class CrossoveredBudgetLines(models.Model):
    _inherit = 'crossovered.budget.lines'

    def _compute_practical_amount(self):
        for line in self:
            acc_ids = line.general_budget_id.account_ids.ids
            date_to = line.date_to
            date_from = line.date_from
            if line.analytic_account_id.id:
                analytic_line_obj = self.env['account.analytic.line']
                domain = [('account_id', '=', line.analytic_account_id.id),
                          ('date', '>=', date_from),
                          ('date', '<=', date_to),
                          ]
                if acc_ids:
                    for budget in line.general_budget_id.budget_line_ids:
                        domain += ['|','&','&',
                                ('move_id.account_id', '=', budget.account_id.id),
                                ('move_id.dimension_name_id', '=', budget.dimension_name_id.id),
                                ('move_id.dimension_value_id', '=', budget.dimension_value_id.id)]
                    domain.pop(-6)

                where_query = analytic_line_obj._where_calc(domain)
                analytic_line_obj._apply_ir_rules(where_query, 'read')
                from_clause, where_clause, where_clause_params = where_query.get_sql()
                select = "SELECT SUM(amount) from " + from_clause + " where " + where_clause

            else:
                aml_obj = self.env['account.move.line']
                domain = [('date', '>=', date_from),
                          ('date', '<=', date_to),
                          ('move_id.state', '=', 'posted')
                          ]
                for budget in line.general_budget_id.budget_line_ids:
                    domain += ['|','&','&',
                            ('account_id', '=', budget.account_id.id),
                            ('dimension_name_id', '=', budget.dimension_name_id.id),
                            ('dimension_value_id', '=', budget.dimension_value_id.id)]
                domain.pop(-6)

                where_query = aml_obj._where_calc(domain)
                aml_obj._apply_ir_rules(where_query, 'read')
                from_clause, where_clause, where_clause_params = where_query.get_sql()
                select = "SELECT sum(credit)-sum(debit) from " + from_clause + " where " + where_clause

            self.env.cr.execute(select, where_clause_params)
            line.practical_amount = self.env.cr.fetchone()[0] or 0.0
    
    
    def action_open_budget_entries(self):
        if self.analytic_account_id:
            # if there is an analytic account, then the analytic items are loaded
            action = self.env['ir.actions.act_window']._for_xml_id('analytic.account_analytic_line_action_entries')
            action['domain'] = [('account_id', '=', self.analytic_account_id.id),
                                ('date', '>=', self.date_from),
                                ('date', '<=', self.date_to)
                                ]
            if self.general_budget_id:
                for budget in self.general_budget_id.budget_line_ids:
                    action['domain'] += ['|','&','&',
                            ('move_id.account_id', '=', budget.account_id.id),
                            ('move_id.dimension_name_id', '=', budget.dimension_name_id.id),
                            ('move_id.dimension_value_id', '=', budget.dimension_value_id.id)]
                action['domain'].pop(-6)
        
        else:
            # otherwise the journal entries booked on the accounts of the budgetary postition are opened
            action = self.env['ir.actions.act_window']._for_xml_id('account.action_account_moves_all_a')
            action['domain'] = [('date', '>=', self.date_from),
                                ('date', '<=', self.date_to)
                                ]
            for budget in self.general_budget_id.budget_line_ids:
                action['domain'] += ['|','&','&',
                        ('account_id', '=', budget.account_id.id),
                        ('dimension_name_id', '=', budget.dimension_name_id.id),
                        ('dimension_value_id', '=', budget.dimension_value_id.id)]
            action['domain'].pop(-6)
        return action

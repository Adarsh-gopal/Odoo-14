from odoo import api, fields, models, tools, _

class SalePrintWiz(models.TransientModel):
    _name = 'sale.print.wiz'
    _description = "Sale print wizard"

    @api.model
    def default_get(self,fields):
        res=super(SalePrintWiz,self).default_get(fields)
        res['saleorder_id'] = self.env.context.get('active_id')
        return res


    saleorder_id = fields.Many2one('sale.order', string='Sale Order')
    state = fields.Char(string='State', compute='get_sale_state',store=True)


    @api.depends('saleorder_id')
    def get_sale_state(self):
        for rec in self:
            if rec.saleorder_id:
                rec.state = rec.saleorder_id.state



    def action_confirm(self):
        rprt_type = self.env.context.get('report_type')
        if rprt_type == 'wqwot':
            return self.env.ref('sales_quotation.sales_quotation_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wqwt':
            return self.env.ref('sales_quotation.woo_quote_with_breakup_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wqexp':
            return self.env.ref('sales_quotation.woo_quote_with_export_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wqwod':
            return self.env.ref('sales_quotation.woo_quote_with_breakup_report_wo_disc').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wqewod':
            return self.env.ref('sales_quotation.woo_quote_with_export_report_wodisc').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wpwt':
            return self.env.ref('sales_quotation.pro_forma_with_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wpwot':
            return self.env.ref('sales_quotation.pro_forma_wo_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wpexp':
            return self.env.ref('sales_quotation.pro_forma_wo_report_export').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wswt':
            return self.env.ref('sales_quotation.sale_order_with').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wswot':
            return self.env.ref('sales_quotation.sale_order_wo_report').report_action(self.saleorder_id, config=False)
        elif rprt_type == 'wsxp':
            return self.env.ref('sales_quotation.sale_order_export1').report_action(self.saleorder_id, config=False)
            



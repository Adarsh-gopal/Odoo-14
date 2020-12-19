from odoo import api, fields, models, tools, _
from odoo.tools.misc import get_lang

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None

class amount(models.Model):
    _inherit="sale.order"

    taxes = fields.Char(string='Total Taxes')
    port_of_discharge = fields.Many2one('contact.port',string='Port of Dishcharge')
    mode_of_delivery = fields.Many2one('mode.of.delivery',string='Mode Of Delivery')
    port_of_loading = fields.Many2one('contact.port',string='Port of Loading')
    # country_of_origin = fields.Char(string='Country of Origin')
    country_of_origin = fields.Many2one('res.country',string='Country of Origin',default=lambda self: self.env.company.country_id.id)

    @api.onchange('partner_id')
    def _onchange_port(self):
        if self.partner_id:
            self.port_of_discharge = self.partner_id.port_of_discharge
            self.mode_of_delivery = self.partner_id.mode_of_delivery
            self.port_of_loading = self.partner_id.port_of_discharge
    



    def print_taxes(self):
        print('\n\n\n',self.amount_by_group,'\n\n\n')


    def amount_to_text(self, amount):
        self.ensure_one()
        def _num2words(number, lang):
            try:
                return num2words(number, lang='en').title()
            except NotImplementedError:
                return num2words(number, lang='en').title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.currency_id.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)
        

        lang_code = self.env.context.get('lang') or self.env.user.lang or get_lang(self.env).code
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        # amount_words = 'Rupees '+ num2words(integer_value)+ ' And '+num2words(fractional_value) + ' Paise only'

        amount_words =self.currency_id.currency_unit_label+' '+ (tools.ustr('{amt_value} {amt_word}').format(
                                    amt_value=_num2words(integer_value, lang=lang.iso_code),
                                    amt_word=self.currency_id.currency_unit_label,
                                    )).replace(self.currency_id.currency_unit_label,' ')
        if not self.currency_id.is_zero(amount - integer_value):
            amount_words += ' ' + _('and ') + self.currency_id.currency_subunit_label + tools.ustr(' {amt_value} {amt_word}').format(
                        amt_value=_num2words(fractional_value, lang=lang.iso_code),
                        amt_word=self.currency_id.currency_subunit_label,
                        ).replace(self.currency_id.currency_subunit_label,' ')
        return amount_words + ' Only'
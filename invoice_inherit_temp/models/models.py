# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InvoiceInherit(models.Model):
    _inherit = "account.move.line"

    Government_total = fields.Float(string="Total Government Fee")
    Government_id = fields.Many2one('product.template')
    Government = fields.Float(string="Government", related='Government_id.Government')

    @api.change('Government_total')
    def _compute_age(self):
        print("TEST")

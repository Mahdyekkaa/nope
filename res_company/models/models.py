# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'

    Government_Fee = fields.Many2one('account.account',
                                     domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]")

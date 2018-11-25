# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Cas(models.Model):
    _name = 'athp.product.cas'

    code = fields.Char(string="CAS Registration Number", required=True)
    name = fields.Char(string="Product CAS Name", required=True)

class ChemicalGroup(models.Model):
    _name = 'athp.chemical.group'

    code = fields.Char(string="Identifier", required=True)
    name = fields.Char(string="Name", required=True)

class ProductProduct(models.Model):
    _inherit = 'product.template'

    athp_stock_ok = fields.Boolean(string="Operated as Chemical stock", default=True)
    cas_id = fields.Many2one('athp.product.cas', string="CAS Registration")
    chemical_group_ids = fields.Many2many('athp.chemical.group', string="Chemical Group")
    external_code = fields.Char(string="External Reference")


# class athp_stock(models.Model):
#     _name = 'athp_stock.athp_stock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
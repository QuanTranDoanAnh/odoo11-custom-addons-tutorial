from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    barcode = fields.Char(string='Barcode')

    @api.onchange
    def _onchange_barcode_scan(self):
        print(self.barcode)

class StockMove(models.Model):
    _inherit = 'stock.move'

    barcode = fields.Char(string='Barcode')

    @api.onchange
    def _onchange_barcode_scan(self):
        print(self.barcode)
        product_rec = self.env['product.product']
        if self.barcode:
            product = product_rec.search([('barcode', '=', self.barcode)])
            self.product_id = product.id
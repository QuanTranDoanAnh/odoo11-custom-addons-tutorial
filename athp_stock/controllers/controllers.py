# -*- coding: utf-8 -*-
from odoo import http

# class AthpStock(http.Controller):
#     @http.route('/athp_stock/athp_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/athp_stock/athp_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('athp_stock.listing', {
#             'root': '/athp_stock/athp_stock',
#             'objects': http.request.env['athp_stock.athp_stock'].search([]),
#         })

#     @http.route('/athp_stock/athp_stock/objects/<model("athp_stock.athp_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('athp_stock.object', {
#             'object': obj
#         })
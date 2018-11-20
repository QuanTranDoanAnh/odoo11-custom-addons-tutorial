from odoo import models, fields, api

class MinimalWizard(models.TransientModel):
    _name = "minimal_wiz.wizard"

    name = fields.Char('Name', required=True)

    @api.multi
    def create_request(self):
        print("You click Finish")

        return {
            'warning': {
                'title': "Your action",
                'message': "You click Finish"
            }
        }
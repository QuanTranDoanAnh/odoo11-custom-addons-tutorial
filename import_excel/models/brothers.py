from odoo import models, fields, api
import xlrd
from datetime import datetime
import base64

class Family(models.Model):
    _name = 'import_excel.family'

    name = fields.Char(string='Family Name', required=True)
    address = fields.Char(string="Family Address", required=True)
    brother_ids = fields.One2many('import_excel.brother', 'family_id', string="Brothers")
    num_brothers = fields.Integer(string="Number of Brothers", compute='_compute_num_brothers', store=True)

    @api.onchange('brother_ids')
    def brother_ids_change(self):
        print(len(self.brother_ids))
        return {}

    @api.depends('brother_ids')
    def _compute_num_brothers(self):
        self.num_brothers = len(self.brother_ids)

    @api.multi
    def launch_import_brothers_wizard(self):
        print("Launching wizard")
        print(self.env.ref('import_excel.view_import_brothers_wizard',False).id)
        view_id = self.env['import_excel.brother.import.wizard']
        new = view_id.create({'family_id':self.id})
        print("In Family")
        print(self.id)
        context = dict(self._context, family_id=self.id)
        return {
                'type': 'ir.actions.act_window',
                'name': 'Import Brothers',
                'res_model': 'import_excel.brother.import.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'res_id'    : new.id,
                'view_id': self.env.ref('import_excel.view_import_brothers_wizard',False).id,
                'target': 'new',
                'context': context
            }

class Brother(models.Model):
    _name = 'import_excel.brother'

    code = fields.Char('Code')
    name = fields.Char(string='Short Name')
    full_name = fields.Char(string='Full Name')
    age = fields.Integer(string="Age")
    birthday = fields.Date('Date of Birth')
    family_id = fields.Many2one('import_excel.family')

class FamilyImportBrothers(models.TransientModel):
    _name = 'import_excel.brother.import.wizard'

    def _default_family(self):
        print("In wizard")
        print(self._context.get('active_id'))
        print("Get default family")
        return self.env['import_excel.family'].browse(self._context.get('family_id'))

    import_file = fields.Binary(string='Import File')
    family_id = fields.Many2one('import_excel.family', string="Family", default=_default_family)
    brother_ids = fields.Many2many('import_excel.brother', string='Brothers')

    @api.multi
    def action_import_brothers(self):
        print("Doing import")
        file_name = datetime.today().strftime('%Y%m%d%H%M%S')
        self.ensure_one()
        data = base64.b64decode(self.import_file)
        with open('/tmp/' + file_name, 'wb') as file:
            file.write(data)
        xl_workbook = xlrd.open_workbook(file.name)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        # Number of columns
        num_cols = xl_sheet.ncols
        print(num_cols)
        # header
        headers = []
        for col_idx in range(0, num_cols):
            cell_obj = xl_sheet.cell(0, col_idx)
            headers.append(cell_obj.value)
        import_data = []
        for row_idx in range(1, xl_sheet.nrows): # Iterate through rows
            row_dict = {}
            for col_idx in range(0, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                row_dict[headers[col_idx]] = cell_obj.value
            import_data.append(row_dict)
        print(import_data)
        for row in import_data:
            self.brother_ids |= self.env['import_excel.brother'].new({
                'code': row['Code'],
                'name': row['Name'],
                'full_name': row['Full Name'],
                'age': row['Age']
            })
        print(self.family_id.brother_ids)
        self.family_id.brother_ids |= self.brother_ids
        return {}
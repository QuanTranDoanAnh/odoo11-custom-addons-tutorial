# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging
import xlrd
import base64
import odoo.addons.decimal_precision as dp
from datetime import datetime, date, timedelta
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)

class ImportExcelWizard(models.TransientModel):
    _name = "import_excel.wizard"
    _description = "Import Excel file"

    upload_file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")

    # import xls file button
    @api.multi
    def action_import(self):
        self.ensure_one()
        data = base64.b64decode(self.upload_file)
        with open('/tmp/' + self.file_name, 'wb') as file:
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


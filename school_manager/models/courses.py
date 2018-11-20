from odoo import models, fields, api

class Course(models.Model):
    _name = 'school_manager.course'

    name = fields.Char('Course Name')
    number = fields.Integer('Course Number')
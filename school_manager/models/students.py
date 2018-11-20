from odoo import models, fields, api

class Student(models.Model):
    _name = 'school_manager.student'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    email = fields.Char('Email')
    number = fields.Integer('Student Number')
    mark_ids = fields.One2many('school_manager.mark', 'student_id', 'Marks')
    level = fields.Char('Level')
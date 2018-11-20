from odoo import models, fields, api

class StudentWizard(models.TransientModel):
    _name = 'school_manager.student.wizard'

    def _get_default_students(self):
        return self.env['school_manager.student'].browse(self.env.context.get('active_ids'))

    student_ids = fields.Many2many('school_manager.student', string='Student', default=_get_default_students)
    level = fields.Char('Level')

    @api.multi
    def set_student_level(self):
        for record in self:
            if record.student_ids:
                for student in record.student_ids:
                    student.level = self.level
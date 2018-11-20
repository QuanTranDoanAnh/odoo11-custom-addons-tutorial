from odoo import models, fields, api
from odoo import exceptions

class Mark(models.Model):
    _name = 'school_manager.mark'

    student_id = fields.Many2one('school_manager.student', 'Student')
    course_id = fields.Many2one('school_manager.course', 'Course')
    exam1 = fields.Float('Exam 1')
    exam2 = fields.Float('Exam 2')
    extra = fields.Float('Discipline & Presence')
    average = fields.Float('Average Mark', compute='_get_avg_mark', store=True)

    @api.multi
    @api.constrains('exam1','exam2','extra')
    def _check_marks(self):
        self.ensure_one()
        if self.exam1 or self.exam2 or self.extra > 20:
            raise exceptions.ValidationError("marks must not be above 20 !!")
    
    @api.multi
    @api.depends('exam1', 'exam2', 'extra')
    def _get_avg_mark(self):
        if self.exam1 and self.exam2 and self.extra:
            self.average = (self.exam1 + self.exam2 + self.extra) / 3
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TaskModel(models.Model):
    _name = 'task_app.task_model'
    _description = 'Task Model'

    name = fields.Char("Task Name", required=True)
    is_done = fields.Boolean('Is done?', default=False)
    active = fields.Boolean('Is active?', default=True)
    category = fields.Many2one("task_app.category_model", "Category")


    def changeState(self):
        self.ensure_one()
        self.is_done = not self.is_done

    def cleanFinished(self):
        records = self.search([("active","=",False)])
        for rec in records:
            rec.unlink()



# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    stage_closed = fields.Boolean(related='stage_id.closed', string='Closed',
                                  readonly=True)
    project_state = fields.Selection(related='project_id.state',
                                     string='Project State',
                                     readonly=True)

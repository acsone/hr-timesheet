# -*- coding: utf-8 -*-
# Copyright 2016 Sunflower IT <http://sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCompany(models.Model):
    """Add hours per day to company"""
    _inherit = 'res.company'

    timesheet_hours_per_day = fields.Float(
        string='Timesheet Hours Per Day',
        digits=(2, 2), default=8.0)
    timesheet_holiday_use_calendar = fields.Boolean(
        string="Use Employee Working Time when creating timesheet",
        help="If checked and a working time schedule is linked to the "
        "employee, use the informations provided by this schedule when "
        "creating the analytic lines for the holidays.",
    )

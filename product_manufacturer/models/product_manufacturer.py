# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer = fields.Many2one(comodel_name='res.partner', string='Manufacturer')
    manufacturer_pname = fields.Char(string='Manuf. Product Name')
    manufacturer_pref = fields.Char(string='Manuf. Product Code')
    manufacturer_purl = fields.Char(string='Manuf. Product URL')

    dqr_date = fields.Date(string='DQR Date')
    dqr_reviewed = fields.Boolean(string='DQR Reviewed')

    labor_cost = fields.Float(string='Labor Cost')
    deb_cost = fields.Float(string='Deburring Cost')
    sand_cost = fields.Float(string='Sanding Cost')
    shipping_cost = fields.Float(string='Shipping Cost')
    machining_cost = fields.Float(string='Machining Cost')






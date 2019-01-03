# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookTags(models.Model):
    _name = 'library_management.booktags'

    tagname = fields.Char()
    color_index = fields.Integer()

class Books(models.Model):
    _name = 'library_management.books'

    name = fields.Char()
    description = fields.Text()
    tags = fields.Many2many('library_management.booktags', string='Tags')

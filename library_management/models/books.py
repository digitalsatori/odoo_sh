# -*- coding: utf-8 -*-

from odoo import models, fields


class BookTags(models.Model):
    _description = "Tags for library books"
    _name = 'library_management.booktags'
    _rec_name = 'tagname'

    tagname = fields.Char()
    color_index = fields.Integer()


class Books(models.Model):
    _description = "Library Books"
    _name = 'library_management.books'

    name = fields.Char()
    description = fields.Text()
    tags = fields.Many2many('library_management.booktags', string='Tags')

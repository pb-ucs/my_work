
from odoo import models, fields

class LibraryIssue(models.Model):
    _name = 'library.issue'
    _description = 'Library Issue'

    name = fields.Char(string="Issue Reference")    
    book_id = fields.Many2one('library.book', string="Book", required=True)
    member_id = fields.Many2one('library.member', string="Member", required=True)
    issue_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    test = fields.Char()

    

# classical inheritance (between different models)
class LibraryBook(models.Model):
    _name = 'book.extension'
    _inherit = 'library.book'
    
    test3 = fields.Char()
    test4 = fields.Char()
    test5 = fields.Char()
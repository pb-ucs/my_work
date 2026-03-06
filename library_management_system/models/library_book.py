
from odoo import models, fields,api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Title")
    # name = fields.Char(string="Title")
    author = fields.Char()
    price = fields.Float()
    ISBN = fields.Char()
    publisher = fields.Char()
    category = fields.Char()
    language = fields.Char()
    available_copies = fields.Integer(default=1)
    status = fields.Selection([
            ('Start', 'start'),
            ('Draft','draft'),
            ('Confirmed','confirmed'),
            ('Cancel','cancel')],default='Start')


    def action_draft(self):
        self.status = 'Draft'
        
    def action_confirmed(self):
        self.status = 'Confirmed'

    def action_cancel(self):
        self.status = 'Cancel'

    def action_start(self):
        self.status = 'Start'

    def action_update(self):
        self.price = 1000

    def action_create(self):
        data = [{'name':'test13'}]
        self.env['library.book'].create(data)


# # extension inheritance  (same model inheritance)
# class Library(models.Model):  # can change name of class nut not model
#     _inherit = 'library.book'

#     test1 = fields.Char()
#     test2 = fields.Char()

# # classical inheritance (between different models)
# class LibraryBook(models.Model):
#     _name = 'book.extension'
#     _inherit = 'library.book'
    
#     test3 = fields.Char()
#     test4 = fields.Char()
#     test5 = fields.Char()

# delegation inheritance


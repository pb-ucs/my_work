from odoo import models, fields, api


class OrmStudent(models.Model):
    _name = 'orm.student'
    _description = 'ORM Student'

    name = fields.Char(required=True)
    l_name = fields.Char()
    email = fields.Char()
    dob = fields.Date()
    cgpa = fields.Float()
    fees_paid = fields.Boolean()
    department_id = fields.Many2one(
            'orm.department',
            string='Department'
        )

    # # def custom(self):
    # #     print('custom method clicked')
    # #     data = [{'name':'written'}]
    # #     self.env['orm.student'].create(data)

    # def write(self, vals):
    #     print(self)
    #     print(vals)
    #     rtn = super(OrmStudent,self).write(vals)
    #     print(rtn) 
    #     return rtn 

    # @api.model_create_multi
    # def create(self, vals_list):
    #     # pass
    #     print('create method called')
    #     print('vals before create', vals_list)
    #     return super(OrmStudent,self).create(vals_list)

    @api.model_create_multi
    # def create(self, vals_list):
    #     # print(self)                         #for my understanding (it will print model name)
    #     # print(vals_list)                    #for my understanding (it will print fields which were entered)
    #     return super().create(vals_list)

    def write(self, vals):
        print(self)                             #for my understanding (it will print model name with its id which was clicked)
        print(vals_list)                             #for my understanding (it will print fields which were changed)
        update = super(OrmStudent,self).write(vals_list)
        # update = super().write(vals)
        print(update)                           #for my understanding (returns True or False)
        return update

    def duplicate(self):
        print(self)
        duplicate = self.copy()
        print('Duplicated:', duplicate)

    def delete_rec(self):
        print('unlink method called')
        print(self)
        # a = self.env['orm.student'].browse(5)
        # print(a)
        rtn = super(OrmStudent,self).unlink() 
        print(rtn)
        return rtn

    def custom_search(self):
        # print (self.search([]))
        # print (self.search([],limit=10,offset=3,order='name'))

        #search
        # print('custom method clicked')
        # print(self)
        # print (self.env['orm.student'].search([]))

        # #search_count
        # total_rec = self.env['orm.student'].search_count([])
        # print(total_rec) 

        #read
        # print(self)
        # print(self.read())                                # prints only recorddata for a particukar id
        # rec = self.env['orm.student'].search([])
        # print(rec.read(fields=['name','fees_paid']))      # prints only provided fields
        # # print(self.env['college.student'].read())           # it should print clicked record id (but its not working)

        # #read_group([domain],[fields],[gruop by],[offset],[limit],[order])  
        students = self.env['orm.student'].read_group([],['name','fees_paid'],['l_name'])
        for stud in students:
            print(stud)

        # #Search_read
        # obj = self.env['orm.student'].search_read()
        # print(obj)                  # prints data  for whole recordset

        # #filter
        # rec = self.env['orm.student'].search([])
        # obj = rec.filtered(lambda r: 'it' in r.name)
        # print(obj)

        # #sorted
        # rec = self.env['orm.student'].search([])
        # a  = rec.sorted(key= lambda r: r.name)  
        # # a  = rec.sorted(key= lambda r: r.name,reverse=True)  
        # print(a)    
        # b  = rec.sorted(key= lambda r: r.id)      
        # # b  = rec.sorted(key= lambda r: r.id,reverse=True)      
        # print(b)    

        # # mapped
        # rec = self.env['orm.student'].search([])
        # fees_done = rec.mapped('name')
        # print(fees_done)

        #name_search
    def name_search(self,name,domain=None,operator='ilike',limit=None,order=None):
        print('name_search')
        print(name,domain,operator,limit,order)
        domain = ['|',('name',operator,name),('department_id',operator,name)]
        rtn = self.search(domain,limit=limit,order=order)
        print(rtn)
        return rtn

       # name_get
    def name_get(self):
        print(self)
        res = []
        for rec in self:
            name = rec.name
            res.append((rec.id, name, rec.department_id))
        print(res)
        return res

        #flush
    def flush(self):
        insert = self.env['orm.student'].create({
            'name': 'testingggg',
            'fees_paid': 'True',
            'department_id':'2',
        })
        print(insert)               # prints record id
        rtn = self.env.cr.flush()   # Force ORM changes to be written to terminal
        print(rtn)















        

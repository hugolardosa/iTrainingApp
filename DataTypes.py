from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email, name, password, address, city, cell_phone, postal_code):
        self.id = id(self)
        self.email = email
        self.name = name 
        self.password = password
        
        self.address = address
        self.city = city
        self.cell_phone = cell_phone
        self.postal_code = postal_code
      
class Client(User):
    def __init__(self, email, name, password, address, city, cell_phone, postal_code, bday, weight, height, obj, health_problems):
        super().__init__(email, name, password, address, city, cell_phone, postal_code)
        self.bday = bday
        self.weight = weight
        self.height = height
        self.obj = obj    
        self.health_problems = health_problems
        self.pt_id = 0
        self.train_list = [] 
        self.pt_code = 0 

class Pt(User):
    def __init__(self, email, name, password, pt_code, address, city, cell_phone, postal_code):
        super().__init__(email, name, password, address, city, cell_phone, postal_code)
        self.client_id = 0
        self.pt_code = pt_code 
class Trains:
    def __init__(self, name, date, duration):
        self.name = name
        self.date = date
        self.duration = duration
        self.needed_objects = []
        self.exerc_list = []

class Exercice:
    def __init__(self, action, times):
        self.action = action
        self.times = times
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
    
    def __str__(self):
        return "Client name: " + self.name  + "email "  + self.email  + "city: "  + self.city  +  "obj: "  + self.obj  + " problems: "  + self.health_problems
class Pt(User):
    def __init__(self, email, name, password, pt_code, address, city, cell_phone, postal_code):
        super().__init__(email, name, password, address, city, cell_phone, postal_code)
        self.client_id = []
        self.pt_code = pt_code
    
    def __str__(self):
        return "Pt name: " + self.name  + "email "  + self.email  + "city: "  + self.city  +  "obj: "  + self.obj  + " problems: "  + self.health_problems

class Trains:
    def __init__(self, name, date, duration, exerc_list=[]):
        self.name = name
        self.date = date
        self.duration = duration
        self.exerc_list = exerc_list
        self.done = False

class Exercice:
    def __init__(self, action, times):
        self.action = action
        self.times = times
        self.needed_objects = []

class Utils:
    def getAlltype(lista, ty=Pt):
        return [ x for x in lista if isinstance(x, ty) ]
# +====== SOME SOLID PRINCIPLES EXAMPLES WITH PYTHON =========+

# +========================= 1 ===============================+
# +=========== Single Responsibility Principle ===============+
# +===========================================================+

# -------------------- Before Applying SRP --------------------

class Person:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"Person(name={self.name})"

    @classmethod
    def save_person(self,person):
        return (f"Save the {person} to the database")

# -------------------- After Applying SRP --------------------

class Person:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"Person(name={self.name})"

class PersonDB:
    def save_person(self,person):
        return (f"Save the {person} to the database")

# -------------------------------------------------------------


# +========================= 2 ===============================+
# +================= Open/CLosed Principle ===================+
# +===========================================================+

# -------------------- Before Applying OCP --------------------

class Discount:
    def __init__(self,customer,price):
        self.customer = customer
        self.price = price
    
    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
    
# -------------------- After Applying OCP --------------------

class Discount:
    def __init__(self,customer,price):
        self.customer = customer
        self.price = price
    
    def get_discount(self):
        return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

# -------------------------------------------------------------


# +========================= 3 ===============================+
# +============= Liskov Susbstitution Principle ==============+
# +===========================================================+

# -------------------- Before Applying LSP --------------------

class Rectangle:
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self,width):
        self.width = width
        self.height = width

    def set_height(self,height):
        self.height = height
        self.width = height
        
# -------------------- After Applying LSP --------------------

class Shape:
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def get_area(self):
        return self.side * self.side

# -------------------------------------------------------------


# +========================= 4 ===============================+
# +============ Interface Segregation Principle ==============+
# +===========================================================+

# -------------------- Before Applying ISP --------------------

class Printer:
    def print_document(self,document):
        pass

    def scan_document(self):
        pass

    def fax_document(self,document):
        pass

# -------------------- After Applying ISP --------------------

class Printer:
    def print_document(self,document):
        pass

class Scanner:
    def scan_document(self):
        pass

class FaxMachine:
    def fax_document(self,document):
        pass

# -------------------------------------------------------------


# +========================= 5 ===============================+
# +=========== Dependency Inversion Principle ================+
# +===========================================================+

# -------------------- Before Applying DIP --------------------

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self,receipent,message):
        self.email_service.send_email(receipent,message)

class EmailService:
    def send_email(self,receipent,message):
        #Send Email
        pass

# -------------------- After Applying DIP --------------------

class NotificationService:
    def __init__(self,notification_service):
        self.notification_service = notification_service

    def send_notification(self,receipent,message):
        self.notification_service.send_notification(receipent,message)

class EmailService:
    def send_notification(self,receipent,message):
        #Send Email
        pass

# -------------------------------------------------------------
class PersonPrivateAge:
    def __init__(self, name, age):
        self.name = name
        self._age = age  
    def get_age(self):
        return self._age

person = PersonPrivateAge("Bob", 25)
print(person.get_age()) 

class PersonWithValidation:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 150:
            self._age = new_age
        else:
            print("Error: age must be an integer between 0 and 150")

p = PersonWithValidation("Alice", 25)
print(p.get_age())  
p.set_age(30)
print(p.get_age()) 
p.set_age(-5)       

class PersonSSN:
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ''.join(ch for ch in str(ssn) if ch.isdigit())

    def get_masked_ssn(self):
        s = self.__ssn
        if len(s) < 4:
            return "*" * len(s)
        return "***-**-" + s[-4:]

    def verify_ssn(self, ssn_to_check):
        check = ''.join(ch for ch in str(ssn_to_check) if ch.isdigit())
        return check == self.__ssn

person = PersonSSN("Carol", "123-45-6789")
print(person.get_masked_ssn())       
print(person.verify_ssn("123456789")) 
print(person.verify_ssn("000-00-0000"))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area) 

class Email:
    def __init__(self, address):
        self.address = address

    @property
    def username(self):
        return self.address.split("@")[0] if "@" in self.address else self.address

    @property
    def domain(self):
        return self.address.split("@", 1)[1] if "@" in self.address else ""


email = Email("alice@gmail.com")
print(email.username)  
print(email.domain)    

from datetime import datetime

class PersonFromBirthyear:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        return datetime.now().year - int(self.birth_year)

    @property
    def can_vote(self):
        return self.age >= 18

person = PersonFromBirthyear("Bob", 2000)
print(f"Age: {person.age}")
print(f"Can vote: {person.can_vote}")

class Score:
    def __init__(self, value=0):
        self._value = 0
        self.value = value  
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, (int, float)) and 0 <= new_value <= 100:
            self._value = int(new_value)
        else:
            print("Error: score must be between 0 and 100")

score = Score(85)
print(score.value)
score.value = 95
print(score.value)  
score.value = 105 

import re

class Username:
    def __init__(self, name):
        self._name = ""
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Error: username must be a string")
            return
        if not (3 <= len(value) <= 20):
            print("Error: username must be 3-20 characters")
            return
        if not re.fullmatch(r"[A-Za-z0-9_]+", value):
            print("Error: username can only contain letters, numbers, and underscore")
            return
        self._name = value

user = Username("alice_123")
print(user.name)   
user.name = "ab"   
user.name = "alice@123" 

import re

class Password:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return "*" * len(self._value) if self._value else None

    @value.setter
    def value(self, password):
        if not isinstance(password, str):
            print("Error: password must be a string")
            return
        checks = [
            (len(password) >= 8, "at least 8 characters"),
            (re.search(r"[A-Z]", password), "an uppercase letter"),
            (re.search(r"[a-z]", password), "a lowercase letter"),
            (re.search(r"[0-9]", password), "a number"),
        ]
        failed = [msg for ok, msg in checks if not ok]
        if failed:
            print("Error: password must contain " + ", ".join(failed))
            return
        self._value = password
        print("Password set")

    def verify(self, password):
        return self._value == password

pw = Password()
pw.value = "Weak1"         
pw.value = "Str0ngPass"     
print(pw.value)              
print(pw.verify("Str0ngPass"))  
print(pw.verify("wrong"))       

class Inventory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0

    @property
    def stock(self):
        return self._stock

    def add_stock(self, quantity):
        if quantity > 0:
            self._stock += quantity
        else:
            print("Quantity must be > 0")

    def remove_stock(self, quantity):
        if quantity <= 0:
            print("Quantity must be > 0")
            return
        if quantity <= self._stock:
            self._stock -= quantity
        else:
            print("Not enough stock")

inv = Inventory("Widgets")
inv.add_stock(100)
inv.remove_stock(30)
print(f"Stock: {inv.stock}")  

class InventoryWithReorder(Inventory):
    def __init__(self, product_name, reorder_point=10):
        super().__init__(product_name)
        self.reorder_point = reorder_point

    @property
    def needs_reorder(self):
        return self._stock < self.reorder_point

    def remove_stock(self, quantity):
        super().remove_stock(quantity)
        if self.needs_reorder:
            print(f"Warning: {self.product_name} needs reorder (stock={self._stock})")

inv2 = InventoryWithReorder("Gadgets", reorder_point=20)
inv2.add_stock(25)
inv2.remove_stock(10)  

from datetime import datetime

class InventoryWithHistory:
    def __init__(self, product_name):
        self.product_name = product_name
        self._stock = 0
        self._history = []

    @property
    def stock(self):
        return self._stock

    @property
    def history(self):
        return list(self._history)  

    def _record(self, action, quantity, reason=""):
        self._history.append({
            "timestamp": datetime.now(),
            "action": action,
            "quantity": quantity,
            "reason": reason,
            "stock_after": self._stock
        })

    def add_stock(self, quantity, reason=""):
        if quantity <= 0:
            print("Quantity must be > 0")
            return
        self._stock += quantity
        self._record("add", quantity, reason)

    def remove_stock(self, quantity, reason=""):
        if quantity <= 0:
            print("Quantity must be > 0")
            return
        if quantity > self._stock:
            print("Not enough stock")
            return
        self._stock -= quantity
        self._record("remove", quantity, reason)

    def get_history_summary(self):
        lines = []
        for e in self._history:
            t = e["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            lines.append(f"{t} | {e['action']} {e['quantity']} | stock_after={e['stock_after']} | {e['reason']}")
        return "\n".join(lines)

invh = InventoryWithHistory("Widgets")
invh.add_stock(50, "initial")
invh.remove_stock(5, "sold 5")
print(invh.stock) 
print(invh.get_history_summary())
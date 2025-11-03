#Unit 1

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

my_car = Car("Toyota", "Camry")
my_car.start()
my_car.honk()


class Vehicle:
    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def start(self):
        print(f"{self.brand} {self.model} is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model, 2)

    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")

# Test
car = Car("Honda", "Civic")
bike = Motorcycle("Yamaha", "R6")
car.start()
bike.start()
bike.wheelie()


class Vehicle:
    vehicle_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.registration_id = None
        Vehicle.vehicle_count += 1

    def register(self, state):
        self.registration_id = f"{state}-{Vehicle.vehicle_count:05d}"
        print(f"{self.brand} {self.model} registered as {self.registration_id}")

class Car(Vehicle):
    def __init__(self, brand, model, doors=4):
        super().__init__(brand, model)
        self.doors = doors

class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity

t1 = Truck("Ford", "F-150", 5000)
t1.register("TX")
c1 = Car("Tesla", "Model 3")
c1.register("CA")

#Unit 2

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}")


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def calculate_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        else: return "F"

class HonorsStudent(Student):
    def calculate_grade(self):
        if self.score >= 95: return "A"
        elif self.score >= 85: return "B"
        elif self.score >= 75: return "C"
        else: return "F"

regular = Student("John", 85)
honor = HonorsStudent("Jane", 75)
print(regular.calculate_grade())  
print(honor.calculate_grade())    


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

    def attack(self):
        return 10

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Health: {self.health}")

class Warrior(Character):
    def attack(self):
        return super().attack() * 2

    def take_damage(self, amount):
        reduced = max(amount - 3, 0)
        super().take_damage(reduced)

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def attack(self):
        if self.mana > 0:
            self.mana -= 10
            return super().attack() * 3
        return super().attack()

war = Warrior("Thor", 100)
mage = Mage("Gandalf", 80, 30)
print(war.attack())  
print(mage.attack()) 
war.take_damage(15)
mage.take_damage(20)

#Unit 3

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Speed: {self.speed} mph")

class SportsCar(Car):
    def __init__(self, brand, model, year, turbo):
        super().__init__(brand, model, year)
        self.turbo = turbo

    def accelerate(self):
        if self.turbo:
            self.speed += 20
        else:
            super().accelerate()
        print(f"Turbo Boost! Speed: {self.speed} mph")

ferrari = SportsCar("Ferrari", "488", 2023, True)
ferrari.accelerate()


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0

    def enroll(self, course):
        self.courses.append(course)
        print(f"Enrolled in {course}")

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic
        self.advisor = None

    def set_advisor(self, advisor_name):
        self.advisor = advisor_name
        print(f"{self.name}'s advisor is now {advisor_name}")

    def enroll(self, course):
        if int(course) >= 500:
            super().enroll(course)
        else:
            print("Graduate students can only enroll in 500-level courses")

grad = GraduateStudent("Alice", "G001", "AI Ethics")
grad.enroll("501")
grad.set_advisor("Dr. Smith")


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

    def start(self):
        print("Starting engine...")

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
        print(f"Car with {doors} doors")

    def start(self):
        super().start()
        print("Car ready to drive")

class ElectricCar(Car):
    def __init__(self, brand, doors, battery_size):
        super().__init__(brand, doors)
        self.battery_size = battery_size
        print(f"ElectricCar with {battery_size} kWh battery")

    def start(self):
        print("Starting silently... Electric mode ready!")

    def charge(self):
        print("Charging battery...")

tesla = ElectricCar("Tesla", 4, 75)
tesla.start()
tesla.charge()

#Unit 4

class Student:
    def __init__(self):
        self.student_id = "S12345"
        self.gpa = 3.5

    def study(self):
        print("Studying hard!")

class Employee:
    def __init__(self):
        self.employee_id = "E67890"
        self.salary = 20000

    def work(self):
        print("Working hard!")

class StudentEmployee(Student, Employee):
    def __init__(self, name):
        Student.__init__(self)
        Employee.__init__(self)
        self.name = name

person = StudentEmployee("Alex")
person.study()
person.work()

class LandVehicle:
    def __init__(self):
        self.speed_on_land = 60

    def drive(self):
        print(f"Driving at {self.speed_on_land} mph")

class WaterVehicle:
    def __init__(self):
        self.speed_on_water = 30

    def sail(self):
        print(f"Sailing at {self.speed_on_water} knots")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, name):
        LandVehicle.__init__(self)
        WaterVehicle.__init__(self)
        self.name = name
        self.mode = "land"

    def switch_mode(self):
        if self.mode == "land":
            self.mode = "water"
            print(f"{self.name} switching to water mode!")
        else:
            self.mode = "land"
            print(f"{self.name} switching to land mode!")

# Test
amphi = AmphibiousVehicle("HydraCar")
amphi.drive()
amphi.switch_mode()
amphi.sail()

class Camera:
    def __init__(self):
        self.megapixels = 12

    def capture(self):
        return "Photo taken!"

class Phone:
    def __init__(self):
        self.phone_number = "555-1234"

    def capture(self):
        return "Screenshot taken!"

class SmartPhone(Phone, Camera):
    def __init__(self, model):
        Phone.__init__(self)
        Camera.__init__(self)
        self.model = model

    def capture(self, mode="phone"):
        if mode == "camera":
            return Camera.capture(self)
        else:
            return Phone.capture(self)

sp = SmartPhone("Galaxy")
print(sp.capture())
print(sp.capture("camera")) 
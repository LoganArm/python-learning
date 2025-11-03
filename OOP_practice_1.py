import gc
import weakref

print("=== UNIT 1: Classes — Book, display_info, Library ===\n")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


my_book = Book("Python Basics", "Jane Doe")
print("Beginner Book Test:")
print("Title:", my_book.title)
print("Author:", my_book.author)
print()

class BookWithDisplay:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"'{self.title}' by {self.author}")

book2 = BookWithDisplay("Effective Python", "Brett Slatkin")
print("Intermediate Book Test:")
book2.display_info()
print()

class BookSimple:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

library = [
    BookSimple("Python Crash Course", "Eric Matthes"),
    BookSimple("Automate the Boring Stuff", "Al Sweigart"),
    BookSimple("Fluent Python", "Luciano Ramalho")
]

print("Advanced Library Test:")
print("Library has", len(library), "books.")
print("Titles:")
for b in library:
    print("-", b.title)
print("\n" + "="*60 + "\n")


print("=== UNIT 2: Constructors, Instance Variables and Instance Methods ===\n")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Camry", 2020)
print("Beginner Car Test:")
print(f"{my_car.year} {my_car.make} {my_car.model}")
print()

class CarWithMileage:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.tank = 10
        self.mpg = 25
        if self.mpg < 0:
            print(f"Error creating car, no car runs on negative mileage")

    def drive(self, miles):
        if miles < 0:
            print("Miles can't be negative.")
            return
        gas_needed = miles /self.mpg
        if self.tank < gas_needed:
            print(f"Ran out of gas after driving {miles} miles.")
            return
        self.mileage 
        print(f"Drove {miles} miles. Total mileage: {self.mileage}")

car2 = CarWithMileage("Honda", "Civic", 2018)
print("Intermediate Car Test:")
car2.drive(120)
car2.drive(30)
print()

class CarFuel:
    def __init__(self, make, model, year, mpg, fuel_tank_gallons=12.0):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
        self.mileage = 0.0
        self.fuel = fuel_tank_gallons
        self.fuel_tank = fuel_tank_gallons

    def drive(self, miles):
        if miles < 0:
            print("Miles must be non-negative.")
            return
        fuel_needed = miles / self.mpg
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.mileage += miles
            print(f"Drove {miles} miles. Mileage: {self.mileage:.1f}. Fuel left: {self.fuel:.2f} gal.")
        else:
            max_miles = self.fuel * self.mpg
            self.mileage += max_miles
            self.fuel = 0.0
            print(f"Not enough fuel for {miles} miles. Drove only {max_miles:.1f} miles and ran out of fuel. Mileage: {self.mileage:.1f}")

    def refuel(self, gallons):
        if gallons <= 0:
            print("Refuel amount must be positive.")
            return
        self.fuel = min(self.fuel + gallons, self.fuel_tank)
        print(f"Refueled. Current fuel: {self.fuel:.2f} gal.")

car3 = CarFuel("Ford", "Focus", 2015, mpg=30, fuel_tank_gallons=13.0)
print("Advanced Car Test:")
car3.drive(100)
car3.drive(300)
car3.refuel(10)
car3.drive(50)
print("\n" + "="*60 + "\n")

print("=== UNIT 3: Object Interactions ===\n")

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

t = Teacher("Mr. Johnson")
t.add_student("Alice")
print("Unit 3 Beginner Teacher Test:")
print("Students:", t.students)
print()

class TeacherManage:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"Added {student_name}")
        else:
            print(f"{student_name} is already in class.")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"Removed {student_name}")
        else:
            print(f"{student_name} not found in class.")

tm = TeacherManage("Ms. Lee")
tm.add_student("Bob")
tm.add_student("Carol")
tm.add_student("Bob")
tm.remove_student("Bob")
tm.remove_student("Zoe")
print("Current students:", tm.students)
print()

class TeacherGrades:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, name, initial_grade=0):
        if name in self.students:
            print(f"{name} already exists.")
        else:
            self.students[name] = initial_grade
            print(f"Added {name} with grade {initial_grade}")

    def grade_student(self, name, grade):
        if name in self.students:
            self.students[name] = grade
            print(f"Updated {name}'s grade to {grade}")
        else:
            print(f"{name} not found.")

    def class_average(self):
        if not self.students:
            return 0.0
        return sum(self.students.values()) / len(self.students)

tg = TeacherGrades("Dr. Adams")
tg.add_student("Alice", 85)
tg.add_student("Bob", 90)
tg.grade_student("Alice", 92)
print("Grades:", tg.students)
print("Class average:", tg.class_average())
print("\n" + "="*60 + "\n")

print("=== UNIT 4: Destructor and Object Lifecycle ===\n")

class BookLifecycle:
    def __init__(self, title):
        self.title = title
        print(f"Book opened: {self.title}")
    def __del__(self):
        print(f"Book closed: {self.title}")

print("Book lifecycle test:")
b = BookLifecycle("Python Fun")
print("Title printed:", b.title)
del b
gc.collect()
print()

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal added: {self.name}")
    def __del__(self):
        print(f"Animal released: {self.name}")

class Zoo:
    def __init__(self):
        self.animals = []
    def add(self, animal):
        self.animals.append(animal)

print("Zoo lifecycle test:")
z = Zoo()
z.add(Animal("Lion"))
z.add(Animal("Monkey"))
print("Zoo animals list:", [a.name for a in z.animals])
del z
gc.collect()
print()

print("Circular reference puzzle test:")

class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None
        print(f"Person created: {self.name}")
    def __del__(self):
        print(f"Person destroyed: {self.name}")

class Dog:
    def __init__(self, name):
        self.name = name
        self.owner = None
        print(f"Dog created: {self.name}")
    def __del__(self):
        print(f"Dog destroyed: {self.name}")

p = Person("Alice")
d = Dog("Buddy")
p.dog = d
d.owner = p
del p
del d
gc.collect()
print()

print("Now fixing circular reference using weakref:")

class Person2:
    def __init__(self, name):
        self.name = name
        self.dog = None
        print(f"Person2 created: {self.name}")
    def __del__(self):
        print(f"Person2 destroyed: {self.name}")

class Dog2:
    def __init__(self, name):
        self.name = name
        self.owner = None
        print(f"Dog2 created: {self.name}")
    def __del__(self):
        print(f"Dog2 destroyed: {self.name}")

p2 = Person2("Carol")
d2 = Dog2("Rex")
p2.dog = d2
d2.owner = weakref.ref(p2)

del p2
del d2
gc.collect()

print("\n=== End of practice problems demonstration ===")

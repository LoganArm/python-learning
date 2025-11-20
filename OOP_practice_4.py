#Unit 1

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color} circle"

class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color} square"

shapes = [Circle("red"), Square("blue"), Circle("green")]
for shape in shapes:
    print(shape.draw())


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        pass

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        return f"Processing ${self.amount:.2f} via credit card ending in {self.card_number[-4:]}"

class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return f"Processing ${self.amount:.2f} via PayPal account {self.email}"

payments = [
    CreditCard(50, "1234567812345678"),
    PayPal(25, "user@example.com")
]
for p in payments:
    print(p.process())

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def save(self, content):
        pass

    def load(self):
        pass

class TextFile(FileHandler):
    def save(self, content):
        print(f"Saving text to {self.filename}.txt")
        self.data = content

    def load(self):
        return self.data

class JsonFile(FileHandler):
    def save(self, content):
        print(f"Converting to JSON and saving to {self.filename}.json")
        self.data = {"data": content}

    def load(self):
        return self.data

class CsvFile(FileHandler):
    def save(self, content):
        print(f"Saving data as CSV to {self.filename}.csv")
        self.data = ",".join(map(str, content))

    def load(self):
        return self.data.split(",")

files = [TextFile("notes"), JsonFile("data"), CsvFile("scores")]
for f in files:
    f.save(["A", "B", "C"])
    print(f.load())


#Unit 2

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starting..."

car = Car("Toyota")
print(car.start())

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    def __init__(self, host):
        self.host = host
        self.connected = False

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self):
        self.connected = True
        print(f"Connected to MySQL at {self.host}")

    def disconnect(self):
        self.connected = False
        print("Disconnected from MySQL")

    def execute_query(self, query):
        if not self.connected:
            print("Error: Not connected!")
        else:
            print(f"MySQL executing: {query}")

class PostgresConnection(DatabaseConnection):
    def connect(self):
        self.connected = True
        print(f"Connected to PostgreSQL at {self.host}")

    def disconnect(self):
        self.connected = False
        print("Disconnected from PostgreSQL")

    def execute_query(self, query):
        if not self.connected:
            print("Error: Not connected!")
        else:
            print(f"Postgres executing: {query}")

# Test
dbs = [MySQLConnection("localhost"), PostgresConnection("127.0.0.1")]
for db in dbs:
    db.connect()
    db.execute_query("SELECT * FROM users;")
    db.disconnect()


from abc import ABC, abstractmethod

class Plugin(ABC):
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.enabled = False

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    @abstractmethod
    def process(self, data):
        pass

class SpellChecker(Plugin):
    def activate(self):
        self.enabled = True
        print(f"{self.name} activated!")

    def deactivate(self):
        self.enabled = False
        print(f"{self.name} deactivated!")

    def process(self, data):
        if not self.enabled:
            print("SpellChecker is not active.")
        else:
            return f"Checked spelling for: {data}"

class AutoSave(Plugin):
    def activate(self):
        self.enabled = True
        print(f"{self.name} activated!")

    def deactivate(self):
        self.enabled = False
        print(f"{self.name} deactivated!")

    def process(self, data):
        if not self.enabled:
            print("AutoSave is not active.")
        else:
            return f"Auto-saved file: {data}"

# Test
spell = SpellChecker("SpellChecker", "1.0")
auto = AutoSave("AutoSave", "2.3")
for plugin in [spell, auto]:
    plugin.activate()
    print(plugin.process("Document.txt"))
    plugin.deactivate()
    





#unit 3

class Calculator:
    def compute(self, x, y):
        return x + y

class ScientificCalculator:
    def compute(self, x, y):
        return x * y

def process_numbers(processor, a, b):
    result = processor.compute(a, b)
    print(f"Result: {result}")

# Test
basic = Calculator()
sci = ScientificCalculator()
process_numbers(basic, 5, 3)
process_numbers(sci, 5, 3)

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Test
for num in Countdown(5):
    print(num)

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Timer started...")
        return self

    def __exit__(self, *args):
        self.end = time.time()
        duration = self.end - self.start
        print(f"Timer stopped. Duration: {duration:.2f} seconds")

    def checkpoint(self):
        print(f"Checkpoint: {time.time() - self.start:.2f} seconds since start")

# Test
with Timer() as t:
    time.sleep(1)
    t.checkpoint()
    time.sleep(1)

#Unit 4

class NotificationStrategy:
    def notify(self, message):
        pass

class EmailNotification(NotificationStrategy):
    def notify(self, message):
        print(f"Email sent: {message}")

class SMSNotification(NotificationStrategy):
    def notify(self, message):
        print(f"SMS sent: {message}")

class App:
    def __init__(self, notifier):
        self.notifier = notifier

    def alert_user(self, message):
        self.notifier.notify(message)

app = App(EmailNotification())
app.alert_user("You have a new message!")
app.notifier = SMSNotification()
app.alert_user("System update available!")

class DataExporter:
    def export(self, data):
        pass

class CSVExporter(DataExporter):
    def export(self, data):
        return ",".join(map(str, data))

class JSONExporter(DataExporter):
    def export(self, data):
        return f'{{"data": {data}}}'

class HTMLExporter(DataExporter):
    def export(self, data):
        rows = "".join(f"<tr><td>{item}</td></tr>" for item in data)
        return f"<table>{rows}</table>"

exporters = [CSVExporter(), JSONExporter(), HTMLExporter()]
data = [1, 2, 3]
for e in exporters:
    print(e.export(data))

import random

class AIStrategy:
    def make_move(self, game_state):
        pass

class AggressiveAI(AIStrategy):
    def make_move(self, game_state):
        return "Attack!"

class DefensiveAI(AIStrategy):
    def make_move(self, game_state):
        return "Defend!"

class RandomAI(AIStrategy):
    def make_move(self, game_state):
        return random.choice(["Attack!", "Defend!", "Retreat!"])

class GameCharacter:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.health = 100

    def play_turn(self, game_state):
        action = self.strategy.make_move(game_state)
        print(f"{self.name} chooses to {action}")

    def change_strategy(self, new_strategy):
        self.strategy = new_strategy
        print(f"{self.name} switched strategy to {new_strategy.__class__.__name__}")

hero = GameCharacter("Arthur", AggressiveAI())
hero.play_turn({})
hero.change_strategy(DefensiveAI())
hero.play_turn({})
hero.change_strategy(RandomAI())
hero.play_turn({})

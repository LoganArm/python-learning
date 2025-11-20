from datetime import datetime
import ast
import re

# --- UNIT 1: Class Methods ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.now().year
        age = current_year - int(birth_year)
        return cls(name, age)


class Config:
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = bool(debug)

    @classmethod
    def from_json_string(cls, json_str):
        normalized = json_str.replace("true", "True").replace("false", "False")
        try:
            data = ast.literal_eval(normalized)
            return cls(data.get('host'), data.get('port'), data.get('debug'))
        except Exception as e:
            raise ValueError("Invalid config string") from e

    @classmethod
    def default_config(cls):
        return cls('localhost', 8080, False)


class User:
    user_count = 0

    def __init__(self, username, email=None):
        self.username = username
        self.email = email
        User.user_count += 1

    @classmethod
    def from_database_row(cls, row):
        username, email = row
        return cls(username, email)

    @classmethod
    def create_guest(cls):
        next_index = cls.user_count + 1
        name = f"guest_{next_index:03d}"
        return cls(name, None)

    @classmethod
    def get_total_users(cls):
        return cls.user_count


# --- UNIT 2: Static Methods ---

class EmailValidator:
    @staticmethod
    def is_valid_email(email):
        if not email or '@' not in email:
            return False
        parts = email.split('@')
        if len(parts) != 2:
            return False
        return '.' in parts[1]

    @staticmethod
    def get_domain(email):
        if not EmailValidator.is_valid_email(email):
            return None
        return email.split('@', 1)[1]


class FileHelper:
    @staticmethod
    def get_extension(filename):
        if '.' not in filename:
            return ''
        return filename.rsplit('.', 1)[1].lower()

    @staticmethod
    def is_image(filename):
        ext = FileHelper.get_extension(filename)
        return ext in ('jpg', 'jpeg', 'png', 'gif')

    @staticmethod
    def make_safe_filename(text):
        text = text.strip().replace(' ', '_')
        safe = re.sub(r'[^A-Za-z0-9._-]', '', text)
        return safe


class CryptoHelper:
    @staticmethod
    def simple_hash(text):
        return sum(ord(c) for c in text)

    @staticmethod
    def caesar_cipher(text, shift):
        result = []
        for ch in text:
            if 'a' <= ch <= 'z':
                base = ord('a')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            elif 'A' <= ch <= 'Z':
                base = ord('A')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                result.append(ch)
        return ''.join(result)

    @staticmethod
    def is_palindrome(text):
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]


# --- UNIT 3: Mixed Methods ---

class Temperature:
    def __init__(self, celsius):
        self.celsius = float(celsius)

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        c = (float(fahrenheit) - 32) * 5/9
        return cls(c)

    @staticmethod
    def is_freezing(celsius):
        return float(celsius) <= 0.0


class UserSystem:
    all_users = []

    def __init__(self, username):
        self.username = username
        self.logged_in = False
        UserSystem.all_users.append(self)

    def login(self, password):
        if password == "secret":
            self.logged_in = True
            return True
        return False

    @classmethod
    def get_active_users(cls):
        return [u for u in cls.all_users if getattr(u, 'logged_in', False)]

    @staticmethod
    def validate_username(username):
        return bool(re.match(r'^[A-Za-z0-9]{3,20}$', username))


class Logger:
    logs = []

    def __init__(self, name):
        self.name = name
        self.enabled = True

    def log(self, message):
        if not self.enabled:
            return
        timestamp = Logger.format_timestamp()
        entry = f"{timestamp} [{self.name}] {message}"
        Logger.logs.append(entry)
        return entry

    @classmethod
    def get_all_logs(cls):
        return list(cls.logs)

    @classmethod
    def clear_logs(cls):
        cls.logs.clear()

    @staticmethod
    def format_timestamp():
        return datetime.now().isoformat(sep=' ', timespec='seconds')

    @staticmethod
    def parse_log_level(message):
        m = re.match(r'^\s*\[(ERROR|WARNING|INFO)\]', message)
        return m.group(1) if m else None


# --- UNIT 4: Factory Pattern ---

class Animal:
    def speak(self):
        raise NotImplementedError()


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        t = animal_type.strip().lower()
        if t == 'dog':
            return Dog()
        if t == 'cat':
            return Cat()
        raise ValueError("Unknown animal type")


class DatabaseConnection:
    def connect(self):
        raise NotImplementedError()


class MySQLConnection(DatabaseConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        return f"Connected to MySQL at {self.host}:{self.port}"


class PostgresConnection(DatabaseConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        return f"Connected to PostgreSQL at {self.host}:{self.port}"


class ConnectionFactory:
    @staticmethod
    def create_connection(db_type, host, port):
        t = db_type.strip().lower()
        if t in ('mysql', 'my_sql'):
            return MySQLConnection(host, port)
        if t in ('postgres', 'postgresql', 'psql'):
            return PostgresConnection(host, port)
        raise ValueError("Unsupported DB type")


class Level:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.enemies = []
        self.treasures = []


class LevelFactory:
    @staticmethod
    def create_easy_level():
        lvl = Level('easy')
        lvl.enemies = ['goblin'] * 3
        lvl.treasures = ['coin'] * 5
        return lvl

    @staticmethod
    def create_hard_level():
        lvl = Level('hard')
        lvl.enemies = ['orc'] * 10
        lvl.treasures = ['gem'] * 2
        return lvl

    @staticmethod
    def create_custom_level(enemies, treasures):
        lvl = Level('custom')
        lvl.enemies = enemies.copy()
        lvl.treasures = treasures.copy()
        return lvl


if __name__ == "__main__":
    print("=== OOP Lecture 5 Practice Problems — \n")

    # --- Class Method Examples ---
    print("• CLASS METHODS")
    person = Person.from_birth_year("Alice", 2000)
    print(f"{person.name} is {person.age} years old")

    config = Config.from_json_string("{'host': 'localhost', 'port': 8080, 'debug': true}")
    print(f"Config parsed -> host={config.host}, port={config.port}, debug={config.debug}")

    default_cfg = Config.default_config()
    print(f"Default config -> host={default_cfg.host}, port={default_cfg.port}, debug={default_cfg.debug}")

    user1 = User.from_database_row(("alice", "alice@email.com"))
    user2 = User.create_guest()
    user3 = User.create_guest()
    print(f"Users created: {user1.username}, {user2.username}, {user3.username}")
    print(f"Total users: {User.get_total_users()}\n")

    # --- Static Method Examples ---
    print("• STATIC METHODS")
    print("Valid email? ->", EmailValidator.is_valid_email("test@gmail.com"))
    print("Email domain ->", EmailValidator.get_domain("user@example.org"))

    print("Extension of 'report.pdf' ->", FileHelper.get_extension("report.pdf"))
    print("Is 'photo.jpg' an image? ->", FileHelper.is_image("photo.jpg"))
    print("Safe filename ->", FileHelper.make_safe_filename("my doc (final).txt"))

    print("Simple hash of 'ABC' ->", CryptoHelper.simple_hash("ABC"))
    print("Caesar cipher (ABC, shift=1) ->", CryptoHelper.caesar_cipher("ABC", 1))
    print("Palindrome check ->", CryptoHelper.is_palindrome("A man, a plan, a canal: Panama"), "\n")

    # --- Mixed Methods ---
    print("• MIXED METHODS")
    temp = Temperature.from_fahrenheit(68)
    print(f"68°F -> {temp.celsius:.1f}°C -> {temp.to_fahrenheit():.1f}°F")
    print("Is -1°C freezing?", Temperature.is_freezing(-1))

    userA = UserSystem("bob")
    userB = UserSystem("carol")
    userA.login("secret")
    print("Active users ->", [u.username for u in UserSystem.get_active_users()])
    print("Validate usernames:", {
        "us": UserSystem.validate_username("us"),
        "user123": UserSystem.validate_username("user123")
    })

    Logger.clear_logs()
    logger = Logger("main")
    logger.log("[INFO] Started")
    logger.log("[ERROR] Something failed")
    print("\nLogs stored:")
    for entry in Logger.get_all_logs():
        print(" ", entry)
    print("Parsed log level ->", Logger.parse_log_level("[ERROR] Disk full!"), "\n")

    # --- Factory Pattern ---
    print("• FACTORY PATTERN")
    pet = AnimalFactory.create_animal("dog")
    print("Pet speaks:", pet.speak())

    db_conn = ConnectionFactory.create_connection("postgres", "db.example.com", 5432)
    print(db_conn.connect())

    easy = LevelFactory.create_easy_level()
    hard = LevelFactory.create_hard_level()
    custom = LevelFactory.create_custom_level(["skeleton", "bat"], ["gem", "coin"])
    print(f"Easy level: {len(easy.enemies)} enemies, {len(easy.treasures)} treasures")
    print(f"Hard level: {len(hard.enemies)} enemies, {len(hard.treasures)} treasures")
    print(f"Custom level: {len(custom.enemies)} enemies, {len(custom.treasures)} treasures")

    print("\n=== End of Lecture 5 ===")

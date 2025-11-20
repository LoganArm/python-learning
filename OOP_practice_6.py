from collections import OrderedDict
import time

# --- UNIT 1: Essential Magic Methods ---

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name} ({len(self)} songs)"

    def __len__(self):
        return len(self.songs)

    def __bool__(self):
        return len(self.songs) > 0


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __len__(self):
        return self.rows * self.cols


# --- UNIT 2: Arithmetic Operator Overloading ---

class Money:
    def __init__(self, dollars):
        self.dollars = dollars

    def __str__(self):
        return f"${self.dollars:.2f}"

    def __add__(self, other):
        return Money(self.dollars + other.dollars)


class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )


# --- UNIT 3: Comparison Operators ---

class Score:
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return f"Score: {self.points}"

    def __eq__(self, other):
        return self.points == other.points

    def __lt__(self, other):
        return self.points < other.points


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year}"

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)


class PriorityItem:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __str__(self):
        return f"{self.data} (P:{self.priority})"

    def __lt__(self, other):
        return self.priority > other.priority 
    def __eq__(self, other):
        return self.priority == other.priority


# --- UNIT 4: Container Protocols ---

class SimpleGrades:
    def __init__(self):
        self.grades = {}

    def __getitem__(self, name):
        return self.grades.get(name, 0)

    def __setitem__(self, name, grade):
        self.grades[name] = grade


class Cache:
    def __init__(self, max_size=3):
        self.data = OrderedDict()
        self.max_size = max_size

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.max_size:
            self.data.popitem(last=False)

    def __contains__(self, key):
        return key in self.data


class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def __getitem__(self, pos):
        return self.data.get(pos, 0)

    def __setitem__(self, pos, value):
        if value != 0:
            self.data[pos] = value
        elif pos in self.data:
            del self.data[pos]

    def __str__(self):
        result = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(str(self[r, c]))
            result.append(' '.join(row))
        return '\n'.join(result)


# --- UNIT 5: Context Managers and Callables ---

class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        print(f"Starting {self.name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"Finished {self.name} in {self.duration:.2f} seconds")

    def get_duration(self):
        return self.duration


class DynamicObject:
    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name):
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._attributes[name] = value

    def __delattr__(self, name):
        if name in self._attributes:
            del self._attributes[name]
        else:
            super().__delattr__(name)

    def __dir__(self):
        return list(self._attributes.keys()) + list(super().__dir__())


class Calculator:
    def __init__(self):
        self.history = []

    def __call__(self, operation, a, b):
        if operation == 'add':
            result = a + b
        elif operation == 'sub':
            result = a - b
        elif operation == 'mul':
            result = a * b
        elif operation == 'div':
            result = a / b if b != 0 else float('inf')
        else:
            raise ValueError("Unknown operation")
        self.history.append(f"{a} {operation} {b} = {result}")
        return result

    def get_history(self):
        return self.history.copy()


if __name__ == "__main__":
    print("OOP Lecture 6 Practice Problems — Solutions Implemented Successfully!\n")
    
    b = Book("Python 101", "Jane Doe", 350)
    print(b)

    pl = Playlist("Favorites")
    pl.add_song("Song A")
    pl.add_song("Song B")
    print(pl)
    print("Playlist has songs?", bool(pl))

    m = Matrix(2, 3)
    print("\nMatrix:")
    print(m)
    print("Matrix length:", len(m))

    money1 = Money(10.50)
    money2 = Money(5.25)
    print("\nMoney sum:", money1 + money2)

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    print("Fractions added:", f1 + f2)
    print("Fractions multiplied:", f1 * f2)

    c1 = Complex(2, 3)
    c2 = Complex(1, -4)
    print("\nComplex add:", c1 + c2)
    print("Complex multiply:", c1 * c2)

    s1, s2 = Score(100), Score(85)
    print("\nScore comparison:", s1 > s2)

    d1, d2 = Date(2024, 5, 1), Date(2024, 5, 2)
    print("Date earlier?", d1 < d2)

    p1, p2 = PriorityItem("Urgent", 10), PriorityItem("Low", 2)
    print("Priority compare:", p1 < p2)

    grades = SimpleGrades()
    grades["Alice"] = 95
    print("\nGrades:", grades["Alice"])

    cache = Cache(max_size=2)
    cache["a"] = 1
    cache["b"] = 2
    cache["c"] = 3 
    print("Cache contains 'a'?", "a" in cache)

    sm = SparseMatrix(2, 2)
    sm[0, 0] = 5
    print("\nSparse matrix:\n", sm)

    with Timer("Example Task"):
        sum(i**2 for i in range(10000))

    obj = DynamicObject()
    obj.name = "Test"
    print("\nDynamic attribute:", obj.name)

    calc = Calculator()
    print("Add:", calc("add", 2, 3))
    print("History:", calc.get_history())

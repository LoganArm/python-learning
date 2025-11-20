from abc import ABC, abstractmethod
import math

# ============================
# Problem 1: Shape Polymorphism
# ============================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        print(f"{name} must be positive!")
        return False


class Circle(Shape):
    def __init__(self, radius):
        if not Shape.validate_positive(radius, "radius"):
            raise ValueError("Invalid radius")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if not Shape.validate_positive(width, "width"):
            raise ValueError("Invalid width")
        if not Shape.validate_positive(height, "height"):
            raise ValueError("Invalid height")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        for (val, name) in [(side1, "side1"), (side2, "side2"), (side3, "side3")]:
            if not Shape.validate_positive(val, name):
                raise ValueError("Invalid triangle side")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)

# ============================
# Problem 2: Pizza System
# ============================

class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not Pizza.validate_size(size):
            raise ValueError("Invalid size")
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        return Pizza.price_list[self.size] + Pizza.topping_price * len(self.toppings)

    def __str__(self):
        return f"{self.size} pizza with {len(self.toppings)} toppings"

    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size, ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size in ['small', 'medium', 'large']


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_id = f"ORDER_{PizzaOrder.total_orders:03d}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(p.calculate_price() for p in self.pizzas)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"


class OrderManager:

    @staticmethod
    def create_order_from_string(order_string):
        order = PizzaOrder()
        items = order_string.split(",")

        for item in items:
            item = item.strip().split()
            size = item[0]
            type_ = item[1]

            if type_ == "margherita":
                order.add_pizza(Pizza.create_margherita(size))
            elif type_ == "pepperoni":
                order.add_pizza(Pizza.create_pepperoni(size))
            elif type_ == "veggie":
                order.add_pizza(Pizza.create_veggie(size))

        return order

    @staticmethod
    def format_receipt(order):
        lines = [
            "=== RECEIPT ===",
            f"Order: {order.order_id}",
            "Items:"
        ]
        for pizza in order.pizzas:
            lines.append(f"  {pizza} - ${pizza.calculate_price()}")
        lines.append(f"Total: ${order.get_total()}")
        lines.append("==============")
        return "\n".join(lines)

# ============================
# Problem 3: Duration Class
# ============================

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Normalize total seconds
        total = hours * 3600 + minutes * 60 + seconds

        if total < 0:
            total = 0

        self.hours = total // 3600
        total %= 3600
        self.minutes = total // 60
        self.seconds = total % 60

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours > 0:
            parts.append(f"{self.hours}h")
        if self.minutes > 0:
            parts.append(f"{self.minutes}m")
        if self.seconds > 0:
            parts.append(f"{self.seconds}s")
        return " ".join(parts) if parts else "0s"

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        return Duration(seconds=self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        new_total = self.total_seconds - other.total_seconds
        return Duration(seconds=max(0, new_total))

    def __mul__(self, multiplier):
        return Duration(seconds=self.total_seconds * multiplier)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds

if __name__ == "__main__":
    print("\n=== Problem 1: Shape Calculator ===")
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    print("\nIndividual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f"  {shape.describe()}")
        print(f"    Area: {shape.area():.2f}")
        print(f"    Perimeter: {shape.perimeter():.2f}")

    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)

    print("\nCollection Totals:")
    print(f"  Total Area: {collection.total_area():.2f}")
    print(f"  Total Perimeter: {collection.total_perimeter():.2f}")

    print("\nTesting validation:")
    try:
        bad = Circle(-5)
    except:
        print("  Correctly rejected negative radius")

    print("\n=== Problem 2: Pizza Orders ===")

    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")

    print("\nIndividual Pizzas:")
    for p in [pizza1, pizza2, pizza3]:
        print(f"  {p} - ${p.calculate_price()}")

    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")

    print("\nOrder from String:")
    order2 = OrderManager.create_order_from_string(
        "large pepperoni, small margherita, medium veggie"
    )
    print(OrderManager.format_receipt(order2))

    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")

    print("\n=== Problem 3: Duration ===")

    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)

    print("\nDurations:")
    print(f"  d1 = {d1}")
    print(f"  d2 = {d2}")
    print(f"  d3 = {d3}")

    print("\nArithmetic:")
    print(f"  d1 + d2 = {d1 + d2}")
    print(f"  d3 - d1 = {d3 - d1}")
    print(f"  d2 * 3 = {d2 * 3}")

    print("\nComparisons:")
    print(f"  d1 == d2? {d1 == d2}")
    print(f"  d1 < d3? {d1 < d3}")
    print(f"  d2 <= d1? {d2 <= d1}")

    durations = [d3, d1, d2]
    durations.sort()
    print("\nSorted durations:")
    for d in durations:
        print(f"  {d}")

    print("\nOverflow Test:")
    d4 = Duration(0, 90, 90)
    print(f"  Duration(0, 90, 90) = {d4}")

    print(f"\nRepr: {repr(d1)}")

# Problem 1
def count_lines(filename):
    """
    Read a file and return the number of lines.
    If the file doesn't exist, return -1.
    Args:
        filename: name of the file to read
    Returns:
        Number of lines in the file, or -1 if file doesn't exist
    Example:
        count_lines("test.txt") → 5 (if file has 5 lines)
        count_lines("missing.txt") → -1 (if file doesn't exist)
    """
def count_lines(filename):
    try:
        with open(filename, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return -1

print(count_lines("test.txt"))     
print(count_lines("missing.txt")) 

#Problem 2
"""
    Create a Rectangle Class with width and height attributes, and methods to calculate area and perimeter.
    """
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 10)
print("Area:", r.area())
print("Perimeter:", r.perimeter()) 


#Problem 3
def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    Args:
        a: numerator (string or number)
        b: denominator (string or number)
    Returns:
        Result of a/b if successful
        "Error: Cannot divide by zero" if b is 0
        "Error: Invalid input" if inputs can't be converted to numbers
    Examples:
        safe_divide(10, 2) → 5.0
        safe_divide("10", "2") → 5.0
        safe_divide(10, 0) → "Error: Cannot divide by zero"
        safe_divide("abc", 2) → "Error: Invalid input"
"""
def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
    except:
        return "Error: Invalid input"

    if b == 0:
        return "Error: Cannot divide by zero"

    return a / b
print(safe_divide(10, 2)) 
print(safe_divide("10", "2")) 
print(safe_divide(10, 0))
print(safe_divide("abc", 2)) 

#Problem 4
def sum_of_digits(n):
    """
    Calculate the sum of all digits in a number using recursion.
    Args:
        n: a positive integer
    Returns:
        Sum of all digits in n
    Examples:
        sum_of_digits(123) → 6 (because 1 + 2 + 3 = 6)
        sum_of_digits(4567) → 22 (because 4 + 5 + 6 + 7 = 22)
        sum_of_digits(5) → 5
        sum_of_digits(0) → 0
    """
def sum_of_digits(n):
    """
    Calculate the sum of all digits in a number using recursion.
    """
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(123)) 
print(sum_of_digits(4567))
print(sum_of_digits(5))
print(sum_of_digits(0)) 

#Problem 5
def process_grades(students):
    """
    Process a list of student dictionaries:
    1. Filter out students with average < 60
    2. Add a letter grade to each remaining student
    3. Sort by average (highest first)
    Args:
        students: list of dictionaries with 'name' and 'grades' keys
    Returns:
        List of processed students with added 'average' and 'letter' keys
    Example Input:

    [
        {'name': 'Alice', 'grades': [90, 85, 95]},
        {'name': 'Bob', 'grades': [50, 45, 55]},
        {'name': 'Charlie', 'grades': [70, 75, 72]}
    ]
    Example Output:
    [
        {'name': 'Alice', 'grades': [90, 85, 95], 'average': 90.0, 'letter':
'A'},
        {'name': 'Charlie', 'grades': [70, 75, 72], 'average': 72.3, 'letter':
'C'}
    ]
    (Bob filtered out because average < 60)
    """
def process_grades(students):
    with_avg = map(lambda s: {**s, "average": sum(s["grades"]) / len(s["grades"])}, students)

    filtered = filter(lambda s: s["average"] >= 60, with_avg)

    graded = map(add_letter_grade, filtered)

    result = sorted(graded, key=lambda s: s["average"], reverse=True)

    return result

def add_letter_grade(student):
    avg = student['average']
    if avg >= 90:
        student['letter'] = 'A'
    elif avg >= 80:
        student['letter'] = 'B'
    elif avg >= 70:
        student['letter'] = 'C'
    else:
        student['letter'] = 'D'
    return student

test_students = [
{'name': 'Alice', 'grades': [90, 85, 95]},
{'name': 'Bob', 'grades': [50, 45, 55]},
{'name': 'Charlie', 'grades': [70, 75, 72]},
{'name': 'Diana', 'grades': [88, 92, 85]}
]
result = process_grades(test_students)

for student in result:
    print(f"{student['name']}: {student['average']:.1f} ({student['letter']})")

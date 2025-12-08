#Problem 1: File Line Counter 
def count_lines_with_word(filename, word):
    """
    Count how many lines in a file contain a specific word.
    The search should be case-insensitive
    
    Parameters:
        filename (str): Name of the filed to read
        word (str): Word to search for
        
    Returns:
        int: Number of lines containing the word
        Returns 0 if file doesn't exist
        
    Example:
        If file contains:
        "Hello world"
        "Python is fun"
        "Hello again"
        count_lines_with_word("file.txt", "hello") returns 2
    """
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
            
                if word.lower() in line.lower():
                    count += 1
    except FileNotFoundError:
        return 0 

    return count



#Problem 2: Bank Account Class
class BankAccount:
    """
    A simple bank account class.
    """

    def __init__(self, owner_name, initial_balance=0):
        """
        Initialize a bank account.
        
        Parameters:
            owner_name (str): Name of account owner
            initial_balance (float): Starting balance (default 0)
        """
        self.owner_name = owner_name
        self.balance = initial_balance


    def deposit(self, amount):
        """
        Add money to the account.
        
        Parameters:
            amount (float): Amount to deposit
        
        Returns:
            float: New balance after deposit
        """
        if amount > 0:
            self.balance += amount
        return self.balance


    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds exist.
        
        Parameters:
            amount (float): Amount to withdraw
        
        Returns:
            float: New balance after withdrawal
            Returns current balance unchanged if insufficient funds
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance


    def get_balance(self):
        """
        Get current balance.
        
        Returns:
            float: Current balance
        """
        return self.balance
    
account = BankAccount("John", 100)
print(account.deposit(50))     # Should print: 150
print(account.withdraw(30))    # Should print: 120
print(account.withdraw(200))   # Should print: "Insufficient funds" then 120


#Problem 3:Safe Calculator
def safe_calculate(num1, num2, operation):
    """
    Perform arithmetic operation with exception handling.
    
    Parameters:
        num1: First number (can be string or number)
        num2: Second number (can be string or number)
        operation (str): One of '+', '-', '*', '/'

    Returns:
        float: Result of the operation
        str: Error message if operation fails
    
    Examples:
        safe_calculate(10, 5, '+') returns 15.0
        safe_calculate("10", "5", '-') returns 5.0
        safe_calculate(10, 0, '/') returns "Error: Division by zero"
        safe_calculate("abc", 5, '+') returns "Error: Invalid number"
        safe_calculate(10, 5, '%') returns "Error: Invalid operation"
    """

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        else:
            return "Error: Invalid operation"

    except ValueError:
        return "Error: Invalid number"

    except ZeroDivisionError:
        return "Error: Division by zero"

print(safe_calculate(10, 5, '+')) # 15.0
print(safe_calculate("10", "5", '-')) # 5.0
print(safe_calculate(10, 0, '/')) # Error: Division by zero
print(safe_calculate("abc", 5, '+')) # Error: Invalid number

#Problem 4: Recursive Palindrome Checker
def is_palindrome_recursive(s):
    """
    Check if a string is a palindrome using recursion.
    Ignore spaces and case.
    
    Parameters:
        s (str): String to check
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Examples:
        is_palindrome_recursive("racecar") returns True
        is_palindrome_recursive("A man a plan a canal Panama") returns True
        is_palindrome_recursive("hello") returns False
        is_palindrome_recursive("") returns True
        is_palindrome_recursive("a") returns True
    """
    s = ''.join(c.lower() for c in s if c != ' ')

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    
    return is_palindrome_recursive(s[1:-1])

print(is_palindrome_recursive("racecar"))       # True
print(is_palindrome_recursive("hello"))         # False
print(is_palindrome_recursive("A man a plan a canal Panama"))            # True
print(is_palindrome_recursive(""))          # True


#Problem 5: Student Grade Analysis
def analyze_grades(students):
    """
    Analyze student grades using map, filter, and lambda functions.
    
    Parameters:
        students: List of tuples (name, [grades])
    
    Returns:
        Dictionary with:
            - 'passing': List of names of students with average >= 70
            - 'failing': List of names of students with average < 70
            - 'highest': Name of student with highest average
            - 'class_average': Average of all student averages
    """

    student_averages = list(map(
        lambda s: (s[0], sum(s[1]) / len(s[1])),
        students
    ))
    
    passing = list(filter(lambda s: s[1] >= 70, student_averages))
    
    failing = list(filter(lambda s: s[1] < 70, student_averages))
    
    highest = max(student_averages, key=lambda s: s[1])[0]
    
    class_avg = sum(s[1] for s in student_averages) / len(student_averages)
    
    return {
        'passing': [s[0] for s in passing],
        'failing': [s[0] for s in failing],
        'highest': highest,
        'class_average': round(class_avg, 1)
    }


test_data = [
    ('Alice', [85, 90, 88]),
    ('Bob', [60, 65, 62]),
    ('Charlie', [75, 80, 77]),
    ('Diana', [95, 92, 94])
]

result = analyze_grades(test_data)
print(result)

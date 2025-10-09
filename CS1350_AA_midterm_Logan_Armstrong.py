import numpy as np
import re

"""
    Create a grade book system with these functions:
    
    1. add_student(gradebook, name, grade)
    -Add a student with their grade
    -Don't add if grade is not between 0-100
    -Return true if added, False otherwise
    
    2. get_class_average(gradebook)
    -Calculate and return the average of all grades
    -Return 0 if gradebook is empty
    
    3. get_passing_students(gradebook)--Bonus
    Return a list of studnet names with grad >= 60
    Return empty lise if none are passing
    
    Example:
    gradebook = {}
    add_student(gradebook, "Alice", 85)
    add_student(gradebook, "Bob", 55)
    add_student(gradebook, "Charlie", 75)
    
    print(get_class_average(gradebook))  
    print(get_passing_students(gradebook))  # Output: ['Alice', 'Charlie']
    """
    #Midterm Problem 1
def add_student(gradebook, name, grade):
    if 0 <= grade <= 100:
        gradebook[name] = grade
        return True
    return False
pass

def get_class_average(gradebook):
    if not gradebook:
        return 0
    return sum(gradebook.values()) / len(gradebook)
pass

def get_passing_students(gradebook):
    return [name for name, grade in gradebook.items() if grade >= 60]
pass

if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85)) 
    print(add_student(gradebook, "Bob", 150))   
    print(add_student(gradebook, "Charlie", 45))   
    
    print(f"Average: {get_class_average(gradebook):2f}")          
    print(f"Passing: {get_passing_students(gradebook)}")
    
    """
    A university needs to track studen course enrollments.
    
    Write these functions:
    
    1. find_common_students(course1_students, course2_students)
    -Return set of students in BOTH courses
    
    2. find_all_studnets(course1_students, course2_students)
    -Return set of students in EITHER course
    
    3. find_unique_to_course1(course1_students, course2_students)
    -Return students ONLY in course1, not in course2
    
    4.*Bonus* check_enrollment(student_name, *course_lists)
    -Check if a students is in ANY of the course lists
    -Return True if found, False otherwise
    -Note: *course_lists means function can take multiple course lists
    
    Example:
    cs_students = {"Alice", "Bob", "Charlie", "David"}
    math_students = {"Charlie", "David", "Eve", "Frank"}
    
    print(find_common_students(cs_students, math_students))  # Should print: {'Charlie', 'David'}
    
    print(check_enrollment("Alice", cs_students, math_students))  # Should print: True
    """
    
    #Midterm Problem 2
def find_common_students(course1_students, course2_students):
    return course1_students.intersection(course2_students)
pass
def find_all_students(course1_students, course2_students):
    return course1_students.union(course2_students)
pass
def find_unique_to_course1(course1_students, course2_students):
    return course1_students.difference(course2_students)
pass
def check_enrollment(student_name, *course_lists):
    return any(student_name in course for course in course_lists)
pass

if __name__ == "__main__":
    cs_students = {"Alice", "Bob", "Charlie", "David"}
    math_students = {"Charlie", "David", "Eve", "Frank"}
    physics_students = {"Alice", "Eve", "George"}
    
    print("Common:", find_common_students(cs_students, math_students))
    print("All:", find_all_students(cs_students, math_students))
    print("CS only:", find_unique_to_course1(cs_students, math_students))
    
    print("Alice enrolled?", check_enrollment("Alice", cs_students, math_students))
    print("Henry enrolled?", check_enrollment("George", cs_students, math_students, physics_students))
    
"""
 You have temperature readings for a week (7 days, 3 times per day).
 Write functions to analyze this data:
 
 1. calculate_daily_averages(temps)
 -temps is a 7x3 array (7 days, 3 readings per day)
    -Return a list of 7 daily averages
    
2. find_hottest_day(temps)
-Return the day index (0-6) with the highest average temperature

3. count_cold_readings(temps, threshold)
-Count how many readings are below the threshold
-Return the count

4. normalize_temperatures(temps)
- Normalize all temperatures to 0-100 scale
- Formula: (temp - min_temp) / (max_temp - min_temp) * 100
- Return normalized array

Example:
import numpy as np
temps = np.array([
    [65, 75, 70],
    [68, 78, 72],
    [70, 80, 75],
    [62, 73, 68],
    [67, 77, 71],
    [69, 79, 74],
    [64, 74, 69]
])
"""
#Midterm Problem 3

def calculate_daily_averages(temps):
    return np.mean(temps, axis=1).tolist()
pass

def find_hottest_day(temps):
    daily_averages = calculate_daily_averages(temps)
    return int(np.argmax(daily_averages))
pass

def count_cold_readings(temps, threshold):
    return int(np.sum(temps < threshold))
pass

def normalize_temperatures(temps):
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    normalized = (temps - min_temp) / (max_temp - min_temp) * 100
    return normalized
pass

if __name__ == "__main__":
    temps = np.array([
        [65, 75, 70],
        [68, 78, 72],
        [70, 80, 75],
        [62, 73, 68],
        [67, 77, 71],
        [69, 79, 74],
        [64, 74, 69]
    ])
    
    print("Daily Averages:", calculate_daily_averages(temps))
    print("Hottest Day Index:", find_hottest_day(temps))
    print("Cold Readings (<70):", count_cold_readings(temps, 70))
    print("Normalized (First Day):", normalize_temperatures(temps)[0])
    
    """
    Clean and validate user input from a regustration form.
    
    Write these functions:
    
    1. clean_name(name)
    -Remove leading/trailing spaces
    -Convert to title case (First letter capitalized)
    -Return cleaned name
    
    2. validate_email(email)
    - Check if email contains exactly one '@'
    - Cehck if there's at least one '.' after '@'
    - Return True if valid, False otherwise
    
    3. format_phone(phone)
    -Remove all non-digit characters
    -If 10 digits, format as (XXX) XXX-XXXX
    -Otherwise return "Invalid"
    
    4. process_registrations(data_string)
    - data_string format: "name,email,phone"
    -Split the string and clean each part
    - Return dictionary with cleaned data or None if invalid
    
    Example:
    data = " john doe , john@email.com, 555-123-4567 "
    result = process_registrations(data)
    # Should return:
    {
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "(555) 123-4567"
    }
    """
#Midterm Problem 4
def clean_name(name):
    return name.strip().title()
pass

def validate_email(email):
    email = email.strip()
    if email.count('@') == 1:
        local, domain = email.split('@')
        if '.' in domain:
            return True
    return False
pass

def format_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return "Invalid"
pass

def process_registrations(data_string):
    parts = data_string.split(',')
    if len(parts) != 3:
        return None
    name, email, phone = parts
    cleaned_name = clean_name(name)
    if not validate_email(email):
        return None
    formatted_phone = format_phone(phone)
    if formatted_phone == "Invalid":
        return None
    return {
        "name": cleaned_name,
        "email": email.strip(),
        "phone": formatted_phone
    }
pass

if __name__ == "__main__":
    
    print(clean_name(" john smith "))
    print(validate_email("test@emal.com"))
    print(validate_email("bad.email"))
    print(format_phone("555-123-4567"))
    print(format_phone("123"))
    
    test_data = " alice jones , alice@example.com, 9871234567"
    print(process_registrations(test_data))
    
    
    """
    Use regular expressions to extract information from text.
    
    Write these functions:
    
    1. find_all_phones(text)
    - Find all phone numbers in format: XXX-XXX-XXXX or (XXX) XXX-XXXX
    -Return list of phone numbers found
    
    2. find_all_prices(text)
    - Find all prices in fomrat: $X.XX or $XX.XX or $XXX.XX
    - Return list of prices as strings (include the $)
    
    3. extract_emails(text)
    - Find all email addresses (simple pattern word@word.word)
    -Return list of email addresses
    
    4. validate_student_id(student_id)
    - Valid format: 2 letters followed by 4 digits (e.g., "CS1234")
    - Return True if valid, False otherwise
    
    Example:
    text = "Contact John at 555-123-4567 or (555) 987-6543.
            Email: john@email.com. Course fee: $150.00"
    print(find_all_phones(text))  
    # Should Print: ["555-123-4567", "(555) 987-6543"]
    """
#Midterm Problem 5

def find_all_phones(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b|\(\d{3}\) \d{3}-\d{4}'
    return re.findall(pattern, text)
pass
def find_all_prices(text):
    pattern = r'\$\d{1,3}\.\d{2}'
    return re.findall(pattern, text)
pass
def extract_emails(text):
    pattern = r'\b\w+@\w+\.\w+\b'
    return re.findall(pattern, text)
pass
def validate_student_id(student_id):
    pattern = r'^[A-Za-z]{2}\d{4}$'
    return bool(re.match(pattern, student_id))
pass
if __name__ == "__main__":
    test_text = """
    Contact John at 555-123-4567 or (555) 987-6543.
    Email us at info@school.edu or admin@college.com
    Course fee: $50.00 for materials, $150.00 for tuition.
    """
    
    print("Phones:", find_all_phones(test_text))
    print("Prices:", find_all_prices(test_text))
    print("Emails:", extract_emails(test_text))
    
    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))
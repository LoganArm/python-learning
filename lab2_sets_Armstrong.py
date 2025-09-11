"""
CS1350 - Week 2, Lab 2: Set Operations
Name: Logan Armstrong
Date: September 7, 2025
Partner: N/a
"""

import time
import random
import string
from collections import Counter

def warmup_1():
    """Create sets from different sources"""
    text = "hello world"
    char_set = set(text)
    even_numbers = {x for x in range(0, 21) if x % 2 == 0}
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = list(set(numbers))
    
    return char_set, even_numbers, unique

def warmup_2():
    """Practice basic set operations"""
    fruits = {'apple', 'banana', 'orange'}
    citrus = {'orange', 'lemon', 'lime'}
    
    citrus_fruits = fruits & citrus
    non_citrus = fruits - citrus
    all_fruits = fruits | citrus
    
    return citrus_fruits, non_citrus, all_fruits

def create_enrollment_data():
    """Create sample enrollment data"""
    enrollments = {
        'CS1350': {'Alice', 'Bob', 'Carol', 'David', 'Eve'},
        'MATH2010': {'Alice', 'Carol', 'Frank', 'Grace'},
        'PHYS1410': {'Bob', 'David', 'Frank', 'Henry'},
        'ENGL1010': {'Eve', 'Grace', 'Henry', 'Ivy'},
        'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
        'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
    }
    
    student_courses = {
        'Alice': {'CS1350', 'MATH2010', 'CHEM1010'},
        'Bob': {'CS1350', 'PHYS1410', 'CHEM1010'},
        'Carol': {'CS1350', 'MATH2010', 'CS2040'},
        'David': {'CS1350', 'PHYS1410', 'CS2040'},
        'Eve': {'CS1350', 'ENGL1010', 'CS2040'},
        'Frank': {'MATH2010', 'PHYS1410'},
        'Grace': {'MATH2010', 'ENGL1010'},
        'Henry': {'PHYS1410', 'ENGL1010'},
        'Ivy': {'ENGL1010', 'CHEM1010'},
        'Jack': {'CHEM1010', 'CS2040'}
    }
    
    return enrollments, student_courses

def find_common_students(course1, course2, enrollments):
    """
    Find students enrolled in both courses.
    Args:
        course1: First course code
        course2: Second course code
        enrollments: Dictionary of course enrollments
    Returns:
        Set of students in both courses
    """
    return enrollments[course1] & enrollments[course2]

def find_popular_combinations(student_schedules):
    """
    Find the most common course pairs taken together.
    Args:
        student_schedules: Dictionary of student course sets
    Returns:
        List of (course_pair, count) tuples, sorted by count
    """
    course_pairs = []
    
    for student, courses in student_schedules.items():
        course_list = list(courses)
        for i in range(len(course_list)):
            for j in range(i + 1, len(course_list)):
                pair = tuple(sorted([course_list[i], course_list[j]]))
                course_pairs.append(pair)
    
    pair_counts = Counter(course_pairs)
    return sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)

def find_exclusive_students(course, enrollments):
    """
    Find students who ONLY take this one course.
    Args:
        course: Course code
        enrollments: Dictionary of course enrollments
    Returns:
        Set of students taking only this course
    """
    other_courses_students = set()
    for other_course, students in enrollments.items():
        if other_course != course:
            other_courses_students |= students
    
    return enrollments[course] - other_courses_students

def recommend_courses(student, student_schedules):
    """
    Recommend courses based on what similar students take.
    Args:
        student: Student name
        student_schedules: Dictionary of student course sets
    Returns:
        Set of recommended courses (not currently taken)
    """
    student_courses = student_schedules[student]
    recommendations = set()
    
    for other_student, other_courses in student_schedules.items():
        if other_student != student and student_courses & other_courses:
            recommendations |= other_courses - student_courses
    
    return recommendations

def test_enrollment_analysis():
    """Test all enrollment analysis functions"""
    print("=== Testing Enrollment Analysis ===")
    
    course_enrollments, student_schedules = create_enrollment_data()
    
    common = find_common_students('CS1350', 'MATH2010', course_enrollments)
    print(f"Students in both CS1350 and MATH2010: {common}")
    assert common == {'Alice', 'Carol'}, "Common students test failed"
    
    popular = find_popular_combinations(student_schedules)
    print(f"Popular course combinations: {popular[:3]}")  # Top 3
    
    exclusive = find_exclusive_students('CS1350', course_enrollments)
    print(f"Students taking only CS1350: {exclusive}")
    
    recommendations = recommend_courses('Frank', student_schedules)
    print(f"Recommended courses for Frank: {recommendations}")
    
    print("All enrollment analysis tests passed!\n")

def process_text(text):
    """
    Process text into a set of words (lowercase, no punctuation).
    Args:
        text: String of text to process
    Returns:
        Set of unique words
    """
    for punct in string.punctuation:
        text = text.replace(punct, ' ')
    
    words = text.lower().split()
    return set(words)

def calculate_similarity(text1, text2):
    """
    Calculate Jaccard similarity between two texts.
    Jaccard = |intersection| / |union|
    Args:
        text1: First text string
        text2: Second text string
    Returns:
        Float between 0 and 1 (1 = identical vocabulary)
    """
    words1 = process_text(text1)
    words2 = process_text(text2)
    
    intersection = words1 & words2
    union = words1 | words2
    
    if not union:
        return 0.0
    
    return len(intersection) / len(union)

def find_unique_words(text1, text2):
    """
    Find words unique to each text.
    Args:
        text1: First text string
        text2: Second text string
    Returns:
        Tuple of (words_only_in_text1, words_only_in_text2)
    """
    words1 = process_text(text1)
    words2 = process_text(text2)
    
    only_in_text1 = words1 - words2
    only_in_text2 = words2 - words1
    
    return only_in_text1, only_in_text2

def detect_common_phrases(texts, min_occurrences=3):
    """
    Find words that appear in at least min_occurrences texts.
    Args:
        texts: List of text strings
        min_occurrences: Minimum number of texts word must appear in
    Returns:
        Set of common words
    """
    word_counts = Counter()
    
    for text in texts:
        words = process_text(text)
        for word in words:
            word_counts[word] += 1
    
    return {word for word, count in word_counts.items() if count >= min_occurrences}

def plagiarism_check(submissions, threshold=0.7):
    """
    Check for potential plagiarism among submissions.
    Args:
        submissions: Dictionary of {student_id: text}
        threshold: Similarity threshold for flagging (0-1)
    Returns:
        List of (student1, student2, similarity) tuples above threshold
    """
    results = []
    students = list(submissions.keys())
    
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            student1, student2 = students[i], students[j]
            similarity = calculate_similarity(submissions[student1], submissions[student2])
            
            if similarity >= threshold:
                results.append((student1, student2, similarity))
    
    return sorted(results, key=lambda x: x[2], reverse=True)

def writing_style_analysis(text):
    """
    Analyze writing style characteristics.
    Args:
        text: Text to analyze
    Returns:
        Dictionary with style metrics
    """
    words = process_text(text)
    all_words = text.lower().split()
    
    clean_words = []
    for word in all_words:
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word:
            clean_words.append(clean_word)
    
    total_word_count = len(clean_words)
    unique_word_count = len(words)
    
    if not words:
        return {
            'vocabulary_size': 0,
            'average_word_length': 0,
            'word_diversity': 0
        }
    
    avg_length = sum(len(word) for word in words) / len(words)
    diversity = unique_word_count / total_word_count if total_word_count > 0 else 0
    
    return {
        'vocabulary_size': unique_word_count,
        'average_word_length': avg_length,
        'word_diversity': diversity
    }

text_samples = {
    'student1': """
    Python is a powerful programming language. It has efficient
    high-level data structures and a simple approach to object-oriented
    programming. Python's elegant syntax and dynamic typing make it
    an ideal language for scripting.
    """,
    'student2': """
    Python is a high-level programming language. It features dynamic
    typing and elegant syntax. Python has simple but effective approach
    to object-oriented programming and powerful data structures.
    """,
    'student3': """
    Java is a class-based, object-oriented programming language. It is
    designed to have as few implementation dependencies as possible. Java
    applications are typically compiled to bytecode.
    """,
    'original': """
    Python is a high-level, general-purpose programming language. Its
    design philosophy emphasizes code readability with the use of
    significant indentation. Python is dynamically typed and garbage-collected.
    """
}


def create_social_network():
    """Create a sample social network"""
    network = {
        'Alice': {'Bob', 'Carol', 'David'},
        'Bob': {'Alice', 'David', 'Eve', 'Frank'},
        'Carol': {'Alice', 'Eve', 'Grace'},
        'David': {'Alice', 'Bob', 'Frank', 'Henry'},
        'Eve': {'Bob', 'Carol', 'Grace', 'Henry'},
        'Frank': {'Bob', 'David', 'Henry', 'Ivy'},
        'Grace': {'Carol', 'Eve', 'Ivy'},
        'Henry': {'David', 'Eve', 'Frank', 'Ivy'},
        'Ivy': {'Frank', 'Grace', 'Henry'}
    }
    return network

def find_mutual_friends(person1, person2, network):
    """
    Find mutual friends between two people.
    Args:
        person1: First person's name
        person2: Second person's name
        network: Social network dictionary
    Returns:
        Set of mutual friends
    """
    return network[person1] & network[person2]

def suggest_friends(person, network, max_suggestions=3):
    """
    Suggest new friends based on mutual connections.
    People with the most mutual friends are suggested first.
    Args:
        person: Person to suggest friends for
        network: Social network dictionary
        max_suggestions: Maximum number of suggestions
    Returns:
        List of (suggested_person, mutual_friend_count) tuples
    """
    current_friends = network[person]
    suggestions = {}
    
    for friend in current_friends:
        for friend_of_friend in network[friend]:
            if friend_of_friend != person and friend_of_friend not in current_friends:
                if friend_of_friend not in suggestions:
                    suggestions[friend_of_friend] = 0
                suggestions[friend_of_friend] += 1
    
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return sorted_suggestions[:max_suggestions]

def find_influencers(network, min_connections=4):
    """
    Find people with at least min_connections friends.
    Args:
        network: Social network dictionary
        min_connections: Minimum number of connections
    Returns:
        Set of influencer names
    """
    return {person for person, friends in network.items() if len(friends) >= min_connections}

def find_isolated_groups(network):
    """
    Find groups of people who are all connected to each other
    but have no connections outside the group.
    Args:
        network: Social network dictionary
    Returns:
        List of sets, each containing an isolated group
    """
    isolated_groups = []
    visited = set()
    
    for person in network:
        if person not in visited:
            group = {person}
            friends = network[person].copy()
            
            all_connected = True
            for friend1 in friends:
                for friend2 in friends:
                    if friend1 != friend2 and friend2 not in network.get(friend1, set()):
                        all_connected = False
                        break
                if not all_connected:
                    break
            
            if all_connected and len(friends) > 0:
                group.update(friends)
                
                has_external = False
                for member in group:
                    for connection in network[member]:
                        if connection not in group:
                            has_external = True
                            break
                    if has_external:
                        break
                
                if not has_external:
                    isolated_groups.append(group)
                    visited.update(group)
    
    return isolated_groups

def test_social_network():
    """Test social network analysis"""
    print("=== Social Network Analysis ===")
    
    social_network = create_social_network()
    
    mutual = find_mutual_friends('Alice', 'Bob', social_network)
    print(f"Mutual friends of Alice and Bob: {mutual}")
    
    suggestions = suggest_friends('Alice', social_network)
    print(f"Friend suggestions for Alice: {suggestions}")
    
    influencers = find_influencers(social_network)
    print(f"Network influencers: {influencers}")
    
    print("Social network analysis completed!\n")


def main():
    """Run all tests and demonstrations"""
    print("CS1350 Lab 2: Set Operations\n")
    

    print("=== Warm-up Exercise Results ===")
    print("Warm-up 1:", warmup_1())
    print("Warm-up 2:", warmup_2())
    print()

    test_enrollment_analysis()
    
    print("=== Text Analysis Results ===")
    print("Plagiarism check results:")
    results = plagiarism_check(text_samples, threshold=0.5)
    for student1, student2, similarity in results:
        print(f"  {student1} vs {student2}: {similarity:.2%} similar")
    
    print("\nWriting style analysis for student1:")
    style = writing_style_analysis(text_samples['student1'])
    for metric, value in style.items():
        print(f"  {metric}: {value:.3f}")
    print()
    
    test_social_network()
    print()

if __name__ == "__main__":
    main()
"""
Day 02 - Python Intermediate
CDSP Data Science Journey

Topics covered:
- lambda
- map
- filter
- reduce
- list/dictionary comprehensions
- nested data
- *args / **kwargs
- exception handling
- files
- JSON
- mini project: Student Data Analyzer
"""

from functools import reduce
import json


# Challenge 1 - map / filter / lambda
numbers = [5, 12, 18, 23, 30, 7, 40, 15]

greater_than_20 = list(filter(lambda x: x > 20, numbers))
times_3 = list(map(lambda x: x * 3, numbers))
greater_than_10_times_2 = list(
    map(lambda x: x * 2, filter(lambda x: x > 10, numbers))
)

names = [" ahmed ", "ALI", "mona", " omar"]
clean_names = list(map(lambda x: x.strip().title(), names))

print(greater_than_20)
print(times_3)
print(greater_than_10_times_2)
print(clean_names)


# Challenge 2 - reduce
values = [2, 3, 4, 5]

total = reduce(lambda a, b: a + b, values)
product = reduce(lambda a, b: a * b, values)
maximum = reduce(lambda a, b: a if a > b else b, values)

print("Sum:", total)
print("Product:", product)
print("Maximum:", maximum)


# Challenge 3 - Comprehensions
numbers = [3, 8, 12, 15, 20, 25, 30, 7, 40]

squares = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
greater_than_15 = [x for x in numbers if x > 15]
squared_evens = [x ** 2 for x in numbers if x % 2 == 0]
squares_dict = {x: x ** 2 for x in numbers}

print(squares)
print(evens)
print(greater_than_15)
print(squared_evens)
print(squares_dict)


# Challenge 4 - Nested data
students = [
    {
        "name": "Ahmed",
        "age": 22,
        "skills": ["Python", "SQL", "Pandas"],
        "scores": {"python": 90, "sql": 85}
    },
    {
        "name": "Ali",
        "age": 24,
        "skills": ["Python", "Excel"],
        "scores": {"python": 80, "sql": 70}
    },
    {
        "name": "Mona",
        "age": 21,
        "skills": ["Python", "Statistics"],
        "scores": {"python": 95, "sql": 88}
    }
]

print(students[0]["name"])
print(students[1]["skills"][0])
print(students[2]["scores"]["python"])

all_names = [student["name"] for student in students]
python_above_85 = [
    student["name"]
    for student in students
    if student["scores"]["python"] > 85
]

python_top_student = max(
    students,
    key=lambda x: x["scores"]["python"]
)

print(all_names)
print(python_above_85)
print("Top Python student:", python_top_student["name"])


# Challenge 5 - *args / **kwargs
def calculate_numbers(*numbers):
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "maximum": max(numbers),
        "minimum": min(numbers)
    }


def student_info(**info):
    for key, value in info.items():
        print(key.title(), ":", value)


def analyze_numbers(*numbers, **options):
    if options.get("show_average"):
        print("Average:", sum(numbers) / len(numbers))
    if options.get("show_max"):
        print("Maximum:", max(numbers))
    if options.get("show_min"):
        print("Minimum:", min(numbers))


print(calculate_numbers(10, 20, 30, 40))
student_info(name="Ahmed", age=22, major="Data Science")
analyze_numbers(10, 20, 30, 40, show_average=True, show_max=True, show_min=True)


# Challenge 6 - Exception handling
try:
    number = int(input("Enter an integer: "))
    print(number)
except ValueError:
    print("Please enter a valid integer.")


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Challenge 7 - Files
students_text = ["Ahmed", "Ali", "Mona", "Omar"]

with open("students.txt", "w", encoding="utf-8") as file:
    for student in students_text:
        file.write(student + "\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Challenge 8 - JSON
student_data = {
    "name": "Ahmed",
    "age": 22,
    "skills": ["Python", "SQL", "Pandas"]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print(loaded_student)


# Mini Project - Student Data Analyzer
students = [
    {
        "name": "Ahmed",
        "age": 22,
        "skills": ["Python", "SQL", "Pandas"],
        "scores": {"python": 90, "sql": 85}
    },
    {
        "name": "Ali",
        "age": 24,
        "skills": ["Python", "Excel"],
        "scores": {"python": 80, "sql": 70}
    },
    {
        "name": "Mona",
        "age": 21,
        "skills": ["Python", "Statistics"],
        "scores": {"python": 95, "sql": 88}
    },
    {
        "name": "Omar",
        "age": 23,
        "skills": ["Python", "SQL"],
        "scores": {"python": 75, "sql": 90}
    }
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

try:
    with open("students.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print("Number of students:", len(data))

    python_scores = [s["scores"]["python"] for s in data]
    sql_scores = [s["scores"]["sql"] for s in data]

    print("Average Python Score:", sum(python_scores) / len(python_scores))
    print("Average SQL Score:", sum(sql_scores) / len(sql_scores))

    top_python = max(data, key=lambda x: x["scores"]["python"])
    print("Top Python Student:", top_python["name"])

    python_above_85 = [
        s["name"] for s in data
        if s["scores"]["python"] > 85
    ]
    print("Python > 85:", python_above_85)

    sql_skill_students = [
        s["name"] for s in data
        if "SQL" in s["skills"]
    ]
    print("Students with SQL skill:", sql_skill_students)

except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON file.")

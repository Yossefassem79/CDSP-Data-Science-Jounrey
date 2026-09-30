"""
Day 01 - Python Basics
CDSP Data Science Journey

Topics covered:
- Variables and data types
- Arithmetic / comparison / logical operators
- Strings
- Conditions
- Loops
- Lists and dictionaries
- Functions
- Basic data analysis with Python
"""

# Challenge 1 - Operators
a = 17
b = 5

print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)


# Challenge 2 - Even numbers
for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# Challenge 3 - List statistics
numbers = [10, 25, 7, 40, 15, 30]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Numbers > 20:", [x for x in numbers if x > 20])


# Challenge 4 - Highest-grade student
students = {
    "Ahmed": 85,
    "Ali": 92,
    "Mona": 88,
    "Omar": 79
}

top_student = max(students, key=students.get)
print("Top student:", top_student)
print("Grade:", students[top_student])


# Challenge 5 - Statistics function
def calculate_stats(numbers):
    return {
        "maximum": max(numbers),
        "minimum": min(numbers),
        "average": sum(numbers) / len(numbers)
    }


print(calculate_stats(numbers))


# Challenge 6 - Product analysis
products = [
    {"name": "Laptop", "price": 30000, "category": "Electronics"},
    {"name": "Phone", "price": 18000, "category": "Electronics"},
    {"name": "Chair", "price": 2500, "category": "Furniture"},
    {"name": "Desk", "price": 5000, "category": "Furniture"}
]

prices = [product["price"] for product in products]

print("Max price:", max(prices))
print("Min price:", min(prices))
print("Average price:", sum(prices) / len(prices))
print("Electronics:", [p for p in products if p["category"] == "Electronics"])


# Challenge 7 - Discount
def calculate_discount(price, discount):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price


print("Final price:", calculate_discount(1000, 20))


# Challenge 8 - Even/Odd analysis
numbers = [10, 15, 22, 7, 30, 41, 18]

even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Even:", even_numbers)
print("Odd:", odd_numbers)
print("Even sum:", sum(even_numbers))
print("Odd sum:", sum(odd_numbers))


# Challenge 9 - Clean names
names = [" ahmed ", "ALI", "mona", " omar"]

clean_names = [name.strip().lower().title() for name in names]
print(clean_names)


# Challenge 10 - Employee analysis
employees = [
    {"name": "Ahmed", "age": 25, "salary": 9000},
    {"name": "Ali", "age": 30, "salary": 12000},
    {"name": "Mona", "age": 22, "salary": 10000},
    {"name": "Omar", "age": 28, "salary": 8000}
]

highest_salary = max(employees, key=lambda x: x["salary"])
youngest_employee = min(employees, key=lambda x: x["age"])

print("Highest salary:", highest_salary)
print("Youngest employee:", youngest_employee)

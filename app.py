# VARIABLES
#  int
# count = 10

# float
# price = 560.90

# string
# name = "josh"

# boolean
# is_student = True

#  TYPES
# name = "joash"
# grade = "A"
# is_student = True

# name = "Jack"
# marks = 90
# print(type(grade))
# print(type(marks))
# print(type(is_student))

# CASTING
# name = input("Enter Your Name: ")
# age = 20
# person = name + " is " + str(age) + " Years Old"
# print(person)

# OPERATORS
# Arithmetic Operators

# addition
# answer = 5 + 5
# print(answer)

# subtraction
# answer = 10 - 5
# print(answer)

# multiplication
# answer = 5 * 5
# print(answer)

# division
# answer = 10 / 5
# print(answer)

# Modulus Returns the Remainder of the Division
# answer = 9 % 4
# print(type(answer))
# print(answer)

# Exponentation Raises a Number to the power of Another
# answer = 2 ** 3
# print(answer)

# Floor Division the ones that Returns the interger part only no Decimal
# results = 9 // 4
# print(results)

# Comparison
# value_1 = 50
# value_2 = 60
# value_3 = 70

# if value_1 == value_2:
#     print("value 1 equals value 2")
# elif value_1 != value_2:
#     print("value 1 is not equal to value 2")
# else:
#     print("Equation Unbalanced")

# if value_1 >= value_2:
#     print("value 1 greater or equals value 2")
# elif value_1 <= value_2:
#     print("value 1 is lesser or equals than value 2")
# else:
#     print("Equation Unbalanced")

# if value_1 > value_2:
#     print("value 1 greater than value 2")
# elif value_1 < value_2:
#     print("value 1 is lesser than value 2")
# else:
#     print("Equation Unbalanced")

# and operator
# age = 20
# marks = 80
# results = (age > 18 and marks > 70)
# print(results)

# results = (age >= 10 or marks >= 90)
# print(results)

# STRINGS
# text = "hello world"
# print(text.upper())

# text = "HELLO WORLD"
# print(text.lower())

# text = "apples,pineapples,banana"
# print(text.split(","))

# sentence = "Python is fun"
# print(sentence.split())

# text = "I love Java"
# print(text.replace("Java", "Python"))

#  LISTS
# my_list = [10, "python", True, 90]
# print(type(my_list))
# print(my_list)

# Append adds an item to the end of the list
# numbers = [90, 10, 20, 30]
# numbers.append(40)
# print(numbers)

# Insert add an items to specific position
# numbers.insert(2, 25)
# print(numbers)

#  Pop removes and returns and item. If no index given removes last Item
# numbers.pop()
# print(numbers)

# Sort arranges the list in ascending order
# numbers.sort()
# print(numbers)

# Sorting in reverse order arranges the list in descending order.
# numbers.sort(reverse=True)
# print(numbers)

# Reverse does not sort; it just flips the current order
# numbers.reverse()
# print(numbers)

# Remove removes the first occurance of specified values
# numbers.remove(30)
# print(numbers)

# TUPLES
# my_tuples = (10, "love", 50.00)
# print(type(my_tuples))

# # Accessing elements
# print(my_tuples[2])

# SETS
# my_sets = {10, 20, 30, "Drama", 30, True}
# print(type(my_sets))

# my_sets.add(50.90)
# print(my_sets)

# my_sets.remove(True)
# print(my_sets)

#  Set Operations
# my_set1 = {1, 2, 3, 4, 5}
# my_set2 = {4, 5, 6, 7, 8}

# 1. Union
# union_set = my_set1 | my_set2
# union_set = my_set1.union(my_set2)
# print(union_set)

# 2. Intersection
# intersection_set = my_set1 & my_set2
# intersection_set = my_set1.intersection(my_set2)
# print(intersection_set)

# 3. Difference
# diffetence_set = my_set1 - my_set2
# diffetence_set = my_set2 - my_set1
# print(diffetence_set)

#  This is an example of a list with duplicate data we wanna convert to a set
# my_list = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, False, "List"]
# my_set = set(my_list)
# print(my_set)

# DICTIONARIES
# Dictionaries store data in key value pairs
# Keys must be uniques and immutable and it's values can be of any type

# Creating a dictionary
# student = {
#     "name": "jack",
#     "age": "21",
#     "major": "Data Science"
# }

# print(type(student))
# print(student)

# Access value by key
# name = student.get("name")
# print(name)

#  Update value
# student["age"] = 22
# print(student)

# Add new value pair
# student["major"] = "Software Engineering"
# print(student)

# looping through Keys
# for key in student.keys():
#     print(key)

# Looping through values
# for value in student.values():
#     print(value)

# CONDITIONALS STATEMENTS
#  if,elif,else
grade = 70

if grade >= 75:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 65:
    print("Grade C")
else:
    print("Grade F")

#  for loops
# Loop through a list
# my_list = ["jack", 12, False, 65.00]
# for list in my_list:
#     print(list)

# Loop with range
# for i in range(1, 9):
#     print(i)

# Break example
# for i in range(1, 100):
#     if i == 50:
#         break
#     print(i)


# FUNCTIONS
# Defined by keyword def
# def greet():
#     print("Good Morning")

# greet()

# arguments & return values
# def sum(a, b):
#     return a + b

# results = sum(5,5)
# print(results)

# IMPORTING LIBRARIES
# Basic imports
# import math

# print(math.sqrt(4))

# Using as alias
# import numpy as np

# FORMATTED STRINGS
name = "Alice"
grade = 80

print(f"Student: {name}, Grade: {grade}")

username = input("Enter Username: ")
print(f"Welcome {username}")

# LIST COMPREHENSION
# This is the general syntax 👉 [expression for item in iterable if condition]

# nums = [ x for x in range(1,10)]
# print(nums)

# nums = [x for x in range(5)]
# print(nums)

# odd = [e for e in range(0, 100) if e % 2 != 0]
# print(f"These are odd Numbers, {odd}")

words = ["ML", "Python", "AI", "Data"]
filtered_words = [w for w in words if len(w) >= 3]
print(filtered_words)

# ERROR HANDLING
try:
    x = int(input("Enter Number: "))
    y = 10/x
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Answer is: {y}")
finally:
    print("Execution finished")

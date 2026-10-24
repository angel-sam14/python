
# Star Pattern
# ------------

# for i in range(1, 5):
#     print("*" * i)

# Reverse a String Using a Loop
# ------------------------------

# text = input("Enter a string: ")
# reverse = ""

# for char in text:
#     reverse = char + reverse

# print("Reversed string:", reverse)


# Even Numbers from 1 to 50
# ---------------------------

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

#  While Loop Questions
# -------------------------

#  Print Numbers from n to 1
# ---------------------------

# n = int(input("Enter a number: "))

# while n >= 1:
#     print(n)
#     n -= 1


# Factorial Using While Loop
# -------------------------

# n = int(input("Enter a number: "))
# fact = 1

# while n > 0:
#     fact *= n
#     n -= 1

# print("Factorial =", fact)


# digit

# num = int(input("Enter a number: "))

# while num > 0:
#     digit = num % 10
#     print(digit)
#     num //= 10

# Count the Number of Digits


# num = abs(int(input("Enter a number: ")))
# count = 0

# if num == 0:
#     count = 1
# else:
#     while num > 0:
#         count += 1
#         num //= 10

# print("Number of digits =", count)

# -----------------------------------------
# while True:
#     text = input("Enter something: ")

#     if text.lower() == "exit":
#         break

#     print(text)

# Loop Control Statements
# ------------------------

# Use break to Find a Number

# numbers = [10, 20, 30, 40, 50]
# target = int(input("Enter number to find: "))

# for num in numbers:
#     if num == target:
#         print("Number found")
#         break
# else:
#     print("Number not found")


# skip even numbers

# for i in range(1, 21):
#     if i % 2 == 0:
#         continue

#     print(i)


# pass

# for i in range(1, 6):
#     pass

# print("Loop completed")


# day

# day = int(input("Enter the day number : "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid day")


# calculator

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# match op:
#     case "+":
#         print("Result =", a + b)
#     case "-":
#         print("Result =", a - b)
#     case "*":
#         print("Result =", a * b)
#     case "/":
#         if b != 0:
#             print("Result =", a / b)
#         else:
#             print("Cannot divide by zero")
#     case _:
#         print("Invalid operator")


# grade

# marks = int(input("Enter marks (0-100): "))

# match marks:
#     case x if 90 <= x <= 100:
#         print("Grade A")
#     case x if 80 <= x < 90:
#         print("Grade B")
#     case x if 70 <= x < 80:
#         print("Grade C")
#     case x if 60 <= x < 70:
#         print("Grade D")
#     case x if 0 <= x < 60:
#         print("Grade F")
#     case _:
#         print("Invalid marks")
# ---------------------------------------------------

# status = int(input("Enter HTTP status code: "))

# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case x if 500 <= x <= 599:
#         print("Server Error")
#     case x if 400 <= x <= 499:
#         print("Client Error")
#     case _:
        # print("Other Status")


# chess board

# row = int(input("Enter row (1-8): "))
# col = int(input("Enter column (1-8): "))

# match (row % 2, col % 2):
    # case (1, 1) | (0, 0):
        # print("Black")
    # case (1, 0) | (0, 1):
        # print("White")


# command parser

# cmd = input("Enter command (add or quit): ").split()

# match cmd:
#     case ["add", a, b]:
#         print("Result =", int(a) + int(b))
#     case ["quit"]:
#         print("Exiting")
#     case _:
#         print("Invalid command")


# file type checker

# filename = input("Enter filename: ")
# parts = filename.split(".")

# match parts:
#     case [name, "jpg" | "png"]:
#         print("Image file")
#     case [name, "py"]:
#         print("Python file")
#     case [name, "pdf"]:
#         print("PDF file")
#     case _:
#         print("Unknown file type")


# calculator

# import math

# shape = input("Enter shape (circle or rect): ").lower()

# if shape == "circle":
#     radius = float(input("Enter radius: "))
#     data = ("circle", radius)
# elif shape == "rect":
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     data = ("rect", length, width)
# else:
#     data = ()

# match data:
#     case ("circle", r):
#         print("Area =", math.pi * r * r)
#     case ("rect", l, w):
#         print("Area =", l * w)
#     case _:
#         print("Invalid shape")


# largest element

# numbers = [10, 5, 25, 8, 15]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest element:", largest)


# smallest element

# numbers = [10, 5, 25, 8, 15]
# smallest = numbers[0]
# for num in numbers:
#     if num < smallest:
#         smallest = num
# print("Smallest element:", smallest)


# sum

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print("Sum:", total)


# average

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)
# print("Average:", average)


# reverse

# numbers = [1, 2, 3, 4, 5]
# reversed_list = []
# for num in numbers:
#     reversed_list = [num] + reversed_list
# print(reversed_list)


# remove duplicates

# numbers = [1, 2, 2, 3, 4, 4, 5]
# result = []
# for num in numbers:
#     if num not in result:
#         result.append(num)
# print(result)


# second largest number

# numbers = [10, 20, 50, 40, 30]
# numbers.sort()
# print("Second largest:", numbers[-2])


# odd or even


# numbers = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# Common Elements Between Two Lists

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for num in list1:
#     if num in list2:
#         common.append(num)

# print("Common elements:", common)


# merge 2 list

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# result = []

# for num in list1 + list2:
#     if num not in result:
#         result.append(num)

# print(result)


# sum


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0

# for row in matrix:
#     for num in row:
#         total += num

# print("Sum:", total)


# largrest element

matrix = [
    [1, 2, 3],
    [10, 5, 6],
    [7, 8, 9]
]

largest = matrix[0][0]

for row in matrix:
    for num in row:
        if num > largest:
            largest = num

print("Largest element:", largest)
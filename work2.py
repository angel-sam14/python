# Traffic light simulator
# -------------------------

# color = input("Enter light color: ").lower()

# if color == "red":
#     print("Stop")
# elif color == "yellow":
#     print("Slow down")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")


# even or odd
# ----------

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Positive, Negative, or Zero
# ------------------------------

# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# even or odd
# ------------

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Voting eligibility
# -------------------

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# Temperature checker
# --------------------

# temp = float(input("Enter temperature: "))

# if temp < 20:
#     print("Cold")
# elif temp <= 30:
#     print("Warm")
# else:
#     print("Hot")

# Leap Year or Not
# -----------------
 
# year = int(input("Enter a year: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# Grade calculator
# -----------------

# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

# Positive and Even

# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("Positive and even")
#     else:
#         print("Not positive or not even")
# else:
#     print("Not positive or not even")


#  Largest of Three Numbers
# -------------------------

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)
# elif b >= a and b >= c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)


# Shop Discount Calculator
# ------------------------

# amount = float(input("Enter purchase amount: "))

# if amount > 5000:
#     discount = amount * 0.20
# elif amount >= 2000:
#     discount = amount * 0.10
# else:
#     discount = 0

# final_bill = amount - discount

# print("Discount =", discount)
# print("Final bill =", final_bill)


# day of the week
# ---------------

# day = int(input("Enter day number: "))

# if day in [1]:
#     print("Sunday")
# elif day in [2]:
#     print("Monday")
# elif day in [3]:
#     print("Tuesday")
# elif day in [4]:
#     print("Wednesday")
# elif day in [5]:
#     print("Thursday")
# elif day in [6]:
#     print("Friday")
# elif day in [7]:
#     print("Saturday")
# else:
#     print("Invalid day")


# Print Numbers from 1 to 10
# --------------------------

# for i in range(1, 11):
#     print(i)


# Multiplication Table
# --------------------

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# Sum of Numbers from 1 to n
# --------------------------

# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Sum =", total)


# Fibonacci Series
# -----------------

# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


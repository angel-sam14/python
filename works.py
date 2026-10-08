# multiplication table
# ---------------------
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(i, "x", num, "=", i * num)

# add two numbers
# ---------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Sum =", a + b)

# difference
# -----------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Difference =", a - b)

# mulitiply three number
# ----------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("Product =", a * b * c)

# division
# ---------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Division =", a / b)

# square
# ------
# num = int(input("Enter a number: "))

# print("Square =", num * num)

# cube
# ----
# num = int(input("Enter a number: "))

# print("Cube =", num * num * num)

# average of 3 number
# --------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("Average =", (a + b + c) / 3)

# price of 5 notebook
# --------------------
# price = int(input("Enter price of one notebook: "))
# print("Total price =", price * 5)

# quotient and remainder
# ----------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Quotient =", a // b)
# print("Remainder =", a % b)

# chocolate
# ----------
# chocolates = 47
# box = 6

# print("Complete boxes =", chocolates // box)
# print("Chocolates left =", chocolates % box)

# minutes
# ---------

# 367seconds
# -----------

# students
# -------
# students = 53
# group = 8

# print("Complete groups =", students // group)
# print("Students left =", students % group)

# last digit of a number
# ---------------------
# num = int(input("Enter a number: "))
# print("Last digit =", num % 10)

# remove last digit
# # -----------------
# num = int(input("Enter a number: "))
# print("Number after removing last digit =", num // 10)

# shopping bill
# -------------
# pens = 3 * 15
# notebooks = 2 * 40

# print("Total bill =", pens + notebooks)

# salary
# -------
# salary = 800
# days = 26

# print("Total salary =", salary * days)

# kilometers
# ----------
# km = int(input("Enter distance in kilometers: "))

# print("Meters =", km * 1000)
# print("Centimeters =", km * 100000)

# rectangle area and centimeter
# -----------------------------
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))

# print("Area =", length * width)
# print("Perimeter =", 2 * (length + width))
# -----------------------------------------------

# 5/10/26
# # --------
# registration
# --------------------
# age = int(input("Enter age: "))
# student = input("Are you a student? yes/no: ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible")
# --------------------------------------------------
# online shopping
# -----------------------

# amount = int(input("Enter order amount: "))
# premium = input("Are you a premium member? yes/no: ")

# if amount >= 3000 or premium == "yes":
#     print("Discount available")
# else:
#     print("No discount")
# --------------------------------------------
# airport
# ----------
# ticket = input("Ticket confirmed? yes/no: ")
# passport = input("Passport valid? yes/no: ")
# hours = int(input("Hours left for departure: "))

# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in available")
# else:
#     print("Online check-in not available")
# ---------------------------------------------------
# movie ticket booking
# -------------------

# age = int(input("Enter age: "))

# if age < 12 or age >= 60:
#     print("Eligible for special ticket price")
# else:
#     print("Not eligible for special ticket price")
# -----------------------------------------------------
# bank loan
# ----------

# income = int(input("Enter monthly income: "))
# score = int(input("Enter credit score: "))
# default = input("Any loan default? yes/no: ")

# if income >= 40000 and score >= 700 and default == "no":
#     print("Eligible for loan")
# else:
#     print("Not eligible")
# -------------------------------------------------
# food delivery
# ------------
# amount = int(input("Enter order amount: "))
# premium = input("Premium member? yes/no: ")
# disabled = input("Delivery disabled? yes/no: ")

# if (amount >= 500 or premium == "yes") and disabled == "no":
#     print("Free delivery")
# else:
#     print("Delivery charge applicable")
# ---------------------------------------------
# employee
# --------
# months = int(input("Enter months in company: "))
# remote = input("Remote work allowed? yes/no: ")

# if months >= 6 and remote == "yes":
#     print("Work from home allowed")
# else:
#     print("Work from home not allowed")
# ------------------------------------------------
# hotel room
# --------------

# available = input("Room available? yes/no: ")
# payment = input("Valid payment? yes/no: ")
# stopped = input("Booking stopped? yes/no: ")

# if available == "yes" and payment == "yes" and stopped == "no":
#     print("Booking can proceed")
# else:
#     print("Booking not allowed")
# -------------------------------------------------
# online exam
# -----------
# login = input("Logged in? yes/no: ")
# registered = input("Exam registered? yes/no: ")
# active = input("Exam active? yes/no: ")
# blocked = input("Account blocked? yes/no: ")

# if login == "yes" and registered == "yes" and active == "yes" and blocked == "no":
#     print("Exam access allowed")
# else:
#     print("Exam access denied")
# -----------------------------------------------
# gym
# -----

# year = int(input("Years subscribed: "))
# active = input("Membership active? yes/no: ")
# yearly = input("Yearly plan purchased? yes/no: ")

# if (year >= 1 and active == "yes") or yearly == "yes":
#     print("Premium upgrade available")
# else:
#     print("Premium upgrade not available")
# -----------------------------------------------------
# ride booking
# ------------

# area = input("Pickup in service area? yes/no: ")
# driver = input("Driver available? yes/no: ")
# scheduled = input("Scheduled rides enabled? yes/no: ")

# if (area == "yes" and driver == "yes") or scheduled == "yes":
#     print("Ride can be booked")
# else:
#     print("Ride cannot be booked")
# -----------------------------------------------------
# e-commerce
# ----------

# days = int(input("Enter days since purchase: "))
# unused = input("Is product unused? (yes/no): ")
# eligible = input("Is product eligible for return? (yes/no): ")

# if days <= 7 and unused == "yes" and eligible == "yes":
#     print("Return accepted")
# else:
#     print("Return rejected")
# -------------------------------------------------
# library 
# ------

# overdue = input("Any overdue book? yes/no: ")
# membership = input("Membership active? yes/no: ")
# book = input("Book available? yes/no: ")

# if overdue == "no" and membership == "yes" and book == "yes":
#     print("Book can be borrowed")
# else:
#     print("Book cannot be borrowed")
# ------------------------------------------------
# job application
# -----------------------

# experience = float(input("Enter Python experience in years: "))
# django = input("Do you know Django? (yes/no): ")
# fastapi = input("Do you know FastAPI? (yes/no): ")

# if experience >= 3 or (experience >= 1 and (django == "yes" or fastapi == "yes")):
#     print("Qualified for next stage")
# else:
#     print("Not qualified for next stage")
# -----------------------------------------------
# mobile data
# ----------

# usage = float(input("Enter data usage percentage: "))
# remaining = float(input("Enter remaining data in GB: "))
# unlimited = input("Is it an unlimited plan? (yes/no): ")

# if (usage >= 90 or remaining < 1) and unlimited == "no":
#     print("Warning: High data usage")
# else:
#     print("No warning")
# ---------------------------------------------------
# parking
# -----------
# pass_valid = input("Do you have a valid parking pass? (yes/no): ")
# visitor = input("Are you paying for visitor parking? (yes/no): ")
# full = input("Is parking lot full? (yes/no): ")

# if (pass_valid == "yes" or visitor == "yes") and full == "no":
#     print("Vehicle can enter")
# else:
#     print("Vehicle cannot enter")
# ------------------------------------------------------------
# scholarship
# -------------
# score = int(input("Enter academic score: "))
# attendance = int(input("Enter attendance: "))

# if (score >= 85 and attendance >= 75) or score >= 95:
#     print("Eligible for scholarship")
# else:
#     print("Not eligible")
# ------------------------------------------------
# food odering
# --------------
# open = input("Restaurant open? yes/no: ")
# delivery = input("Delivery available? yes/no: ")
# online = input("Online orders accepted? yes/no: ")

# if open == "yes" and delivery == "yes" and online == "yes":
#     print("Order can be placed")
# else:
#     print("Order cannot be placed")
# --------------------------------------------------------
# smart home security
# -------------------
# motion = input("Motion detected? yes/no: ")
# door = input("Main door opened? yes/no: ")
# armed = input("Security armed? yes/no: ")

# if armed == "yes" and (motion == "yes" or door == "yes"):
#     print("Security alert")
# else:
#     print("No alert")
# ----------------------------------------------------------
# travel insurance
# ----------------
# age = int(input("Enter age: "))
# days = int(input("Enter trip duration: "))
# covered = input("Destination covered? yes/no: ")
# excluded = input("Destination excluded? yes/no: ")

# if age >= 18 and age <= 65 and days <= 30 and covered == "yes" and excluded == "no":
#     print("Eligible for insurance")
# else:
#     print("Not eligible")
# --------------------------------------------------------------------------------------
# 6/10/26
# ---------
# grade
# -----
# mark = int(input("Enter mark: "))

# if mark >= 90:
#     print("A+")
# elif mark >= 80:
#     print("A")
# elif mark >= 70:
#     print("B")
# elif mark >= 60:
#     print("C")
# elif mark >= 50:
#     print("D")
# else:
#     print("Fail")


# ATM
# ----
# balance = int(input("Enter balance: "))
# amount = int(input("Enter amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter amount in multiples of 100")
# else:
#     print("Withdrawal Successful")


# online delivery
# ---------------
# amount = int(input("Enter order amount: "))

# if amount >= 5000:
#     charge = 0
# elif amount >= 2000:
#     charge = 50
# else:
#     charge = 100

# print("Delivery charge =", charge)
# print("Final amount =", amount + charge)


# employee
# ---------
# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")


# electricity bill
# -----------------
# units = int(input("Enter units: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = 100 * 2 + (units - 100) * 3
# elif units <= 400:
#     bill = 100 * 2 + 100 * 3 + (units - 200) * 5
# else:
#     bill = 100 * 2 + 100 * 3 + 200 * 5 + (units - 400) * 7

# print("Electricity bill =", bill)


# movie ticket
# -------------
# age = int(input("Enter age: "))

# if age < 5:
#     print("Free")
# elif age <= 12:
#     print("Ticket price = 100")
# elif age < 60:
#     print("Ticket price = 200")
# else:
#     print("Ticket price = 120")


# traffic fine
# --------------
# speed = int(input("Enter speed: "))

# if speed <= 60:
#     print("No fine")
# elif speed <= 80:
#     print("Fine = 500")
# elif speed <= 100:
#     print("Fine = 1000")
# else:
#     print("Fine = 2000")
#     print("License Review")


# restaurant biling
# -------------------
# bill = int(input("Enter bill amount: "))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 15 / 100
# elif bill >= 1000:
#     discount = bill * 10 / 100
# else:
#     discount = 0

# final_bill = bill - discount

# print("Discount =", discount)
# print("Final bill =", final_bill)


# college admission 
# ------------------
# score = int(input("Enter entrance score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")


# bank loan
# ----------
# score = int(input("Enter credit score: "))
# default = input("Existing loan default? yes/no: ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# elif score >= 750:
#     print("Low Risk")
# elif score >= 650:
#     print("Medium Risk")
# elif score >= 550:
#     print("High Risk")
# else:
#     print("Very High Risk")


# hotel room 
# ----------
# room = input("Enter room type: ")
# nights = int(input("Enter number of nights: "))

# if room == "Standard":
#     price = 2000
# elif room == "Deluxe":
#     price = 3500
# else:
#     price = 5000

# total = price * nights

# if nights > 5:
#     total = total - total * 10 / 100

# print("Final bill =", total)


# employee
# ---------
# salary = int(input("Enter annual salary: "))
# score = int(input("Enter performance score: "))

# if score >= 90:
#     bonus = salary * 20 / 100
# elif score >= 75:
#     bonus = salary * 15 / 100
# elif score >= 60:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0

# print("Bonus =", bonus)



# mobile data
# ------------
# data = int(input("Enter data usage in GB: "))

# if data < 5:
#     print("Basic Plan - Rs.199")
# elif data <= 20:
#     print("Standard Plan - Rs.399")
# elif data <= 50:
#     print("Premium Plan - Rs.699")
# else:
#     print("Unlimited Plan - Rs.999")



# parking fee
# -------------
# hours = int(input("Enter parking hours: "))
# ev = input("Is it an electric vehicle? yes/no: ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if ev == "yes":
#     fee = fee - fee * 20 / 100

# print("Parking fee =", fee)


# online exam 
# -------------
# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory < 40 or practical < 40:
#     print("Fail")
# else:
#     average = (theory + practical) / 2

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")


# flight
# -------
# weight = int(input("Enter baggage weight: "))
# business = input("Business class? yes/no: ")

# if business == "yes":
#     limit = 25
# else:
#     limit = 15

# if weight <= limit:
#     print("No extra charge")
# elif weight <= 20:
#     print("Charge = 500")
# elif weight <= 30:
#     print("Charge = 1000")
# else:
#     print("Charge = 2000")


# e-commerce
# ------------
# days = int(input("Enter days since purchase: "))
# unused = input("Is product unused? yes/no: ")
# returnable = input("Is product returnable? yes/no: ")

# if days <= 7 and unused == "yes" and returnable == "yes":
#     print("Return Approved")
# elif days > 7:
#     print("Return rejected: More than 7 days")
# elif unused == "no":
#     print("Return rejected: Product is used")
# else:
#     print("Return rejected: Product is not returnable")


# salary
# --------
# salary = int(input("Enter annual salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 5 / 100
# elif salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100

# final_salary = salary - tax

# print("Tax =", tax)
# print("Final salary =", final_salary)


# ride
# ------
# distance = int(input("Enter distance in km: "))
# peak = input("Is it peak hour? yes/no: ")

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = distance * 15
# elif distance <= 30:
#     fare = distance * 12
# else:
#     fare = distance * 10

# if peak == "yes":
#     fare = fare + fare * 20 / 100

# print("Final fare =", fare)


# leave approval
# ---------------
days = int(input("Enter number of available leave days: "))
requested = int(input("Enter number of days requested: "))

if requested > days:
    print("Leave request exceeds available leave days")
elif requested <= 3:
    print("Leave approved")
elif requested <= 7:
    print("Leave requires manager approval")
else:
    print("Leave requires HR approval")
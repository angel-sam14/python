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
# days = int(input("Enter number of available leave days: "))
# requested = int(input("Enter number of days requested: "))

# if requested > days:
#     print("Leave request exceeds available leave days")
# elif requested <= 3:
#     print("Leave approved")
# elif requested <= 7:
#     print("Leave requires manager approval")
# else:
#     print("Leave requires HR approval")

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

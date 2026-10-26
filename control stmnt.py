# 6/10/26
# --------
# CONTROL STMTS

# control statements:is used to control the flow of execution of a program,
# classified into three
# 1)decision making:works on decision making statements like if,if-else,if-elif-else
# 2)loop
# 3)jump stmt

# if:one condition check chythu,condition true anengil athinte block execute chythu,condition false anengil block skip chythu
# if-else:one condition check chythu,condition true anengil if block execute chythu,condition false anengil else block execute chythu
# if-elif-else:multiple condition check chythu,condition true anengil if/elif block execute chythu,condition false anengil else block execute chythu(conditions interconneted akki vekkan)
# nested if:if block inside another if block,if-else block inside another if block,if-elif-else block inside another if block

# INDENTATION:python uses indentation to define a block of code,indentation is the space at the beginning of a code line,indentation is very important in python,if indentation is not proper then it will give an error

# syntax
# ------
#  if condition:
#     # block of code
#     .
#     .
#     .
# if condition:
#     if block
# else:
#    else block

# -----------------------------------------------
# eg: if
# age=17
# if age>=18:
#     print("Adult")

# # if-else
# if age>=18:
#     print("Adult")
# else:
#     print("child")
# print("after if block")

# # if-elif-else
# if age > 0 and age < 13:
#     print("child")
# elif age >= 13 and age < 20:
#     print("teenager")
# elif age >= 20 and age < 60:
#     print("adult")
# elif age >= 60:
#     print("senior citizen")
# else:
#     print("invalid entry")
# print('----------------')


# nested if
# age=int(input("Enter your age:"))
# mark=int(input("Enter your mark:"))
# if age>=18:
#     print("age requirement satisfied...")
#     if mark>=50:
#         print("admission approved...")
#     else:
#         print("Admission rejected:insufficient marks...")    
# else:
#     print("Admission rejected:Age reqirement is not stisfied")

# ----------------------------------------------------------
# Match stmt:match statement is used to match a value against a series of patterns and execute the corresponding block of code,match statement is similar to switch case in other programming languages,match statement is available in python 3.10 and above
# syntax:
# match expression:

#     case value1:
#         # block of code
#     case value2:
#         # block of code
#     case _:
#         # block of code

# eg:
# day=int(input("Enter the number of the day:"))
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7: 
#         print("Saturday")

#     case _:
#         print("Invalid day")    


# -----------------------------------------------
# MARKS
# -----

# mark=int(input("Enter your mark:"))
# if mark >90 and mark <=100:
#     print("A+")
# elif mark >80 and mark <=90:
#     print("A")  
# elif mark > 70 and mark <=80:
#     print("B+")
# elif mark >60 and mark <=70:
#     print("B")
# elif mark >50 and mark <=60:
#     print("C")  
# elif mark >=40 and mark <=50:
#     print("D")
# elif mark < 40 and mark >=0: 
#     print("E")            
# else:
#     print("Invalid mark entry!!!!!!")         
# -------------------------------------------------
# DAY
# -----

# day ="monday"
# match day.capitalize():
#     case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
#         print("Weekday")
#     case "Saturday"|"Sunday":
#         print("Weekend")
#     case _:
#         print("invalid")           

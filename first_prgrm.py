 # print("hello world")
 # 29/9/26
 # -------
 #  # PYTHON DATA TYPES
# # -----------------

# # 1.Text
#    # str
# print('hai')
# print("hello")

# # 2.Numeric
#    # Int
#    # Float
#    # Complex 
# print(45)
# print(-45)
# print(5.6)
# print(4+0j)

# # 3.Boolean
#    # Bool
# print(True)
# print(False)

# # 4.Sequence
#     # List
# print([4,5,6])
#     # Tuple
# print((4,4,6))
#     # Range
# print(range(5))

# # 5.Set
#    # Set
# print({4,5,6})
#    # Frozen set
# print(frozenset([7,5,6]))

# # 6.Mapping
#    # Dict
# print({"rno":5,"name":"Angel"})   

# # 7.Binary
#    # Bytes
# print(b"hello")   
#    # Bytearray
# print(bytearray(b"hello"))  
#    # Memoryview
# print(memoryview(b"hello"))

# # 8.None
#   # None
# print(None)

# # check the data-type of a value

# print(type(b"hello"))
# print(type("hello"))
# ---------------------------------------------------
# creating variables
# ------------------
# name="Angel"
# print(name)

# Variable naming rules
# ----------------------

# case-sensitive
# should not start with a number
# donot use special characters
# should be meaningful
# should not use keywords
# can contain digit,alphabets or _
# snake_case
# should  start with a alphabet,digit or _

# name="Angel"
# _name="Angel"
# my-name="sdd"
# my name=""
# if="yadhu"

# name="Amal"
# print(name)
# is_logged_in =True

# a=b=c=10
# p,q,r=56,96,12

# MUTABLE AND IMUTABLE DATA TYPES
# --------------------
# list  
# set
# dict
   
# OPERATORS
# ----------

# 1.Arithmetic 
# -------------
# addition +
# subtraction -
# multiplication *
# division /
# floor division //
# modulus %
# exponentiation **

# eg:
    # a=10
    # b=3
    # print(a+b)
    # print(a-b)
    # print(a*b)
    # print(a/b)
    # print(a//b)
    # print(a%b)
    # print(a**b)

# print(type(a))
# print(int("544644df"))
# print(int(True))
# print(int(False))

# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(2**3**2)
# print(17//15)
# -----------------------------------
# 1/10/26
# ---------


# --------------------------------------------------------------------------
# 5/10/26
# --------
# STRING:seq of characters enclosed in ""/''/
# slicing:starting index positionum ,ending index position um kodkm,step add chym(positive number kodkknm),-ve number kodthal last inu ahn indexing

# name="Alan Mathew"
# course='python programming'
# address="""
# kochi
# kerala
# india
# """
# # type casting
# rno=str(8)

# print(name,course,address)
# print(type(name))   
# print(type(course))
# print(type(address))

# print(name[0])
# print(address[9])

# # slicing:start,end,step
# print(name[0:5])
# print(course[5:16])
# print(course[5:16:2])
# print(course[1:17:3])

# print(name[-1])
# print(name[-2])

# print(course[-10:-1])
# print(course[-10:-1:2])
# print(course[:5])
# print(course[5])
# print(name[4:])
# print(course[::2])
# print(course[::-1])

# ---------------------------------

# string methods
# --------------
# name="Alan Mathew"
# print(name.upper())
# print(name.lower())
# print(name.capitalize()) 
# print(name.title())
# print(name.swapcase())
# print(name.startswith(('Ala')))
# print(name.endswith('Hew'))
# print(name.isalpha())
# print(name.isdigit())
# print('hfak6455'.isalnum())
# print(name.strip()+'dfdf')
# print(name.lstrip()+'dfdf')
# print(name.rstrip()+'dfdf')

# print(name.split(' '))
# print(name.split('a'))

# # print(9+"hai")
# print('*'*8)

# print("A is",14,",which is greater than 100:",14>100)
# print(f'\n\nA is {14},\twhich is greater than 100: {14>100}')

# ----------------------------------------------------------
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

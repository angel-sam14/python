# 7/10/26
# ---------

# looping stmts
# -------------
# 1)for loop:is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# 2)while loop: is used to execute a block of code as long as a specified condition is true.

# syntax of for loop
# ------------------
# for variable in iterable:
#     body of for loop

# 0-9
# ---
# for i in range(10):
#     print(i)

# 1-10
# -----
# for i in range(1,11):
#     print(i)

# even numbers from 100 to 200
# ----------------------------
# for i in range(100,201):
#     if i%2==0:
#         print(i)

# another way to print even numbers from 100 to 200
# --------------------------------------------------
# for x in range(0,100,2):
#     print(x)

# pattern:1-5
# --------------
# for n in range(1,6):
#     print('*'*n)

# pattern:5-1
# --------------
# for n in range(5,0,-1):
#     print('*'*n)

# another way to print pattern:1-5
# -------------------------------
# x=5
# for n in range(5):
#     print('*'*x)
#     x-=1

#armstrong number: a number that is equal to the sum of cubes of its digits

# while loop
# -----------
# while condition:
    # block of loop

# 1-10
# ----
# n=1
# while n<=10:
#     print(n)
#     n+=1

# pattern:1-5
# --------------
# n=1
# while n<=5:   
#     print('*'*n)
#     n+=1

# pattern:5-1
# --------------
# n=5
# while n>=1:
#     print('*'*n)
#     n-=1

# 8/10/26
# ---------
# jump stmts : is used to transfer the control of execution to another part of the program.
# ----------
# 1)break: is used to terminate the loop and transfer the control to the next statement after the loop.
# 2)continue: is used to skip the current iteration of the loop and transfer the control to the next iteration of the loop.
# 3)pass: is used to skip the current iteration of the loop and transfer the control to the next iteration of the loop.

# break : terminate the loop completely
# -----
# n=1
# while n<=10:
#     if(n==4):
#         break  
#     print(n)
#     n+=1

# continue:skip current iteration  and move  to next iteration
# --------
# n=1
# while n<=10:
#     if(n==4):
#         n+=1
#         continue  
#     print(n)
#     n+=1

# # iteration 1:
# n=1
# 1<=10
# # True
# 1==4 
# # False
# n=2


# iteration 2:
# n=2
# 2<=10
# # True
# 2==4 
# # False
# n=3

# iteration 3:
# n=3
# 3<=10
# # True
# 3==4 
# # False
# n=4


# iteration 4:
# n=4
# 4<=10
# # True
# 4==4 
# # True
# continue

# iteration 5:
# n=5
# 5<=10
# # True
# 5==4 
# # False
# n=6

# # iteration 6:
# n=6
# 6<=10
# # True
# 6==4 
# # False
# n=7

# iteration 7:
# n=7                                      --------->o/p:1 2 3
# 7<=10
# # True
# 7==4 
# # False
# n=8

# iteration 8:
# n=8
# 8<=10 True
# 8==4  False
# n=9

# iteration 9:
# n=9
# 9<=10 True
# 9==4  False
# n=10
# --------------------------------------
# n=1
# while n<=15:
#     if(n==8):
#         n+=1
#         continue  
#     print(n)
#     n+=1


# sum of numbers using loop
# -------------------------

# n =int(input("enter a multi-digit:"))
# sum =0
# while n>0:
#     r=n%10
#     sum += r
#     n //=10
# print(f"sum is {sum}")    

# eg:487

# iteration 1:
# n = 487
# sum = 0
# r = 487 % 10 = 7
# sum = 0 + 7 = 7
# n = 487 // 10 = 48


# iteration 2:
# n = 48
# sum = 7
# r = 48 % 10 = 8
# sum = 7 + 8 = 15
# n = 48 // 10 = 4


# iteration 3:
# n = 4
# sum = 15
# r = 4 % 10 = 4
# sum = 15 + 4 = 19
# n = 4 // 10 = 0

# python collections
# -------------------
# 1)list:is a ordered colllection of hetrogeneous data
# indexed
# allow duplicates
# creating using [ ]

# numbers=[45,87,110,134,155,155]
# print(numbers)
# print(type(numbers))----->type
# print(len(numbers)) ---->length

# print(numbers[3])---->indexing
# print(numbers[0:3])-->step
# print(numbers[0:5:2])---->slicing
# print(numbers[::-1]) --->reverse
# print(numbers[-1]) ----->reverse indexing

# numbers[2] = 1---->replacing numbers
# print(numbers)

# for n in numbers:
#     print(n)

# print('Even numbers')
# for n in numbers:
#     if n%2 == 0:
#         print(n)

# 12/10/26
#---------

# PYTHON LIST METHODS
# -------------------

# 1)append:used to add items at the end of the list

# a = [10, 20, 30]
# a.append(40)
# print(a)

# 2)extend:used to add multiple items to the list(iterable data)

# a = [10, 20]
# a.extend([30, 40])
# print(a)

# 3)insert(1,x):used to add items at specific index

# a = [10, 30]
# a.insert(1, 20)
# print(a)

# 4)remove(x):used to remove specified values from the list

# a = [10, 20, 30]
# a.remove(20)
# print(a)

# 5)pop(i):used to remove item using index position and return the item

# a = [10, 20, 30]
# x = a.pop()
# print(x)
# print(a)

# 6)clear():remove all the items from the list

# a = [10, 20, 30]
# a.clear()
# print(a)

# 7)index(x):return the first occurence of a value(index number)

# a = [10, 20, 30]
# print(a.index(20))

# 8)count(x):returns the count of a value 

# a = [10, 20, 10, 30]
# print(a.count(10))

# 9)sort():sort the items in ascending order/descending

#1)ascending

# a = [30, 10, 20]
# a.sort()
# print(a)

#2)descending

# a.sort(reverse=True)
# print(a)

# 10)reverse:reverse the list items

# a = [10, 20, 30]
# a.reverse()
# print(a)

# 11)copy:creates a shallow copy()

# a = [10, 20, 30]
# b = a.copy()
# print(b)

# ------------------------------------------------

# 10) reverse: reverse the list items

# a = [10, 20, 30]
# a.reverse()
# print(a)


# 11) copy: creates a shallow copy()

# a = [10, 20, 30]
# b = a.copy()
# print(b)


# ------------------------------------------------

#  another example

# names = ["Aryan", "Arun", "Anu", "Meenu", "Jethin"]

# names.append("Priya")
# names.append("Amal")
# names.insert(3, "Athul")
# names.extend(["Pranav", "Sreekanth", "Suriya", "Vijay", "Ajith", "Athul"])
# names.remove("Ajith")
# names.pop(2)

# names.pop()
# del names[8]
# del names
# names.clear()

# print(names.index("Suriya"))
# print(names.count("Athul"))
# # names.sort()
# # names.reverse()

# names.append([1, 2, 3])
# copy_names = names.copy()
# copy_names[5] = "Yamal"
# names[-1][2] = 86

# print(names[-1])
# print(copy_names)
# --------------------------------------------
# specific letter

# names = ["Anu","Anjali","Riya","sangeetha","Aparna","Alona"]
# letter="A"
# result=[]

# for name in names:
#     if name.startswith(letter):
#       result.append(name)
# print(result)
# ---------------------------------------
# another way
# ------------
# for name in names:
#     if name[0]=="A":
#         print(name)
# -------------------------------------------------

# for name in names:
#    if name.startswith('A'): 
#       print(name)

# -------------------------------------------------
#16/10/26
# -------
# sum 
# ---

# n = int(input("Enter a multi-digit number: "))
# sum = 0
# while n > 0:
    # r = n % 10
    # sum += r
    # n //= 10
# else:
    # print(f"Sum is {sum}") 


# Reverse of a number
# --------------------

# n = int(input("Enter a multi-digit number: "))

# rev = 0
# while n > 0:
#     r = n % 10
#     rev = (rev * 10) + r
#     n //= 10
# else:
#     print("Reverse is", rev)


# PALINDROME OR NOT
# ------------------

# n = int(input("Enter a multi-digit number: "))

# run = n

# rev = 0
# while n > 0:
#     r = n % 10
#     rev = (rev * 10) + r
#     n //= 10
# else:
#     print("Reverse is", rev)

# palindrome_or_not = "Palindrome" if run == rev else "Not a Palindrome"

# print(palindrome_or_not)


# LIST COMPREHENSION(even)
# ------------------

# l2 = [45, 86, 97, 41, 37, 54, 28, 36]

# even_numbers = []

# for x in l2:
#     if x % 2 == 0:
#         even_numbers.append(x)

# print(even_numbers)


# List comprehension(squared)
# --------------------------

# l1 = [45, 86, 97, 41, 37, 54, 28, 36]

# new_list = [x for x in l1]

# even_numbers = [x for x in l1 if x % 2 == 0]

# squared_numbers = [x*x for x in l1]

# print(new_list)
# print(squared_numbers)
# print(even_numbers)


#  List Comprehension – Even Numbers from range()
# -----------------------------------------------

# n = 10

# even_numbers = []

# for x in range(0, n+1):
#     if x % 2 == 0:
#         even_numbers.append(x)

# print(even_numbers)

#22/10/26
# -----------

# packing:
# unpacking:tuples ile data vere vere variables ilek assign chym
# t1=(4,5,6,7,8,9,4,4,5,6,4)
# print(t1[4])

# t2=4,5,6, 7,8                #----------->packing
# print(type(t2))
# a,b=(4,5)    # ----------->unpacking
# print(a)
# print(b) 
# # functions in tuple
# # -------------------- 
# name1,name2 ="Abin","Angel"
# print(t1.count(4))
# print(t1.index(4))
# print(t1.index(9))
# print(len(t1))
# for x in t1:
#     print(x)
# # l1 = List('Amal')   
#     # -------------->['a','m','a','l']
# # print(l1)
# # l1[5]=19
# t1=tuple('amal')
# print(t1)

# names=["angel","asdf","dfgh","dfgt"]
# for index,name in enumerate(names):
#     print(index,name)

# print(" ".join(names)) 

# # dictionary:key value pairs

# student = {
#     "name":"Angel",
#     "age":21,
#     "rno":3,
#     "course":"BCA",
#     "course":"BCOM"
# }
# items=student.items()
# # print(student)
# # print(type(student))
# # print(student["age"])
# student=["name"] = "Abin Sam"
# print(student["name"])
# student["email"] = "abinsam@gmail.com"
# # print(student)
# # print("BCA" in student)
# # for x in student:
# #     print(student[x])

# print(student['age'])
# print(student.get['age'])
# print(student.get['agee'])
# print(student.get['agee,20'])
# student.update("hobbies":"writing","reading","dancing")
# student.update("rno":4)
# student.pop()
# student.popitem()
# student.values()
# student.keys()


    
    
# get:data edukkn
# update:new data/key add/edit akkn
# setdefault: existing data puthythayt update chym
# key illnki new add akkm
# allenki default value vrm
# pop:remove/delete chyn
# popitem:last item remove cheyyan
# values:values mathram display chyn(eg:('angel,21....))
# keys:only keys (eg:name,age........)
# items:separated ayt vrm(eg:('name','angel'))
# 


# enumerate:listile index position access chyn
# sep:
# split:list->string
# join:
# key:dictionary il ninn value access chyn
# -----------------------------------------------------------
# ==========================================================
# # 1. TUPLE
# # ==========================================================

# # Definition:
# # A tuple is an ordered and immutable collection of elements.
# # Tuple-il multiple values store cheyyam.
# # Create cheythu kazhinjal values change cheyyan pattilla.


# # 1.1 Tuple Indexing
# # Definition:
# # Indexing is used to access an element using its position.

# t1 = (4, 5, 6, 7, 8, 9, 4, 4, 5, 6, 4)

# print("\n--- Tuple Indexing ---")
# print(t1[4])


# # 1.2 Packing
# # Definition:
# # Packing is combining multiple values into a single tuple.

# t2 = 4, 5, 6, 7, 8

# print("\n--- Packing ---")
# print(t2)
# print(type(t2))


# # 1.3 Unpacking
# # Definition:
# # Unpacking is assigning tuple elements to separate variables.

# a, b = (4, 5)

# print("\n--- Unpacking ---")
# print(a)
# print(b)

# name1, name2 = "Abin", "Angel"
# print(name1)
# print(name2)


# # 1.4 count()
# # Definition:
# # count() returns the number of occurrences of a specified element.

# print("\n--- count() ---")
# print(t1.count(4))


# # 1.5 index()
# # Definition:
# # index() returns the index of the first occurrence of an element.

# print("\n--- index() ---")
# print(t1.index(4))
# print(t1.index(9))


# # 1.6 len()
# # Definition:
# # len() returns the total number of elements.

# print("\n--- len() ---")
# print(len(t1))


# # 1.7 Tuple using for loop
# # Definition:
# # A for loop is used to access each element in a tuple.

# print("\n--- Tuple For Loop ---")
# for x in t1:
#     print(x)


# # 1.8 tuple()
# # Definition:
# # tuple() converts an iterable into a tuple.

# print("\n--- tuple() ---")
# t3 = tuple("amal")
# print(t3)



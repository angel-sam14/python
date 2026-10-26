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


# # ==========================================================
# # 2. LIST
# # ==========================================================

# # Definition:
# # A list is an ordered and mutable collection of elements.
# # List-il values add, remove, update cheyyan pattum.


# # 2.1 list()
# # Definition:
# # list() converts an iterable into a list.

# print("\n--- list() ---")
# l1 = list("Amal")
# print(l1)


# # 2.2 enumerate()
# # Definition:
# # enumerate() returns both the index and the value of each element.

# print("\n--- enumerate() ---")
# names = ["angel", "asdf", "dfgh", "dfgt"]

# for index, name in enumerate(names):
#     print(index, name)


# # 2.3 join()
# # Definition:
# # join() combines strings from an iterable into a single string.

# print("\n--- join() ---")
# print(" ".join(names))
# print(",".join(names))
# print("-".join(names))


# # ==========================================================
# # 3. DICTIONARY
# # ==========================================================

# # Definition:
# # A dictionary is a mutable collection of key-value pairs.
# # Oro key-kkum corresponding value undaakum.


# # 3.1 Dictionary Creation
# # Definition:
# # A dictionary stores data in key-value pairs.

# print("\n--- Dictionary Creation ---")

# student = {
#     "name": "Angel",
#     "age": 21,
#     "rno": 3,
#     "course": "BCA"
# }

# print(student)
# print(type(student))


# # 3.2 Accessing Dictionary Values
# # Definition:
# # Dictionary values can be accessed using their keys.

# print("\n--- Accessing Values ---")
# print(student["name"])
# print(student["age"])


# # 3.3 Adding New Data
# # Definition:
# # A new key-value pair can be added using assignment.

# print("\n--- Adding Data ---")
# student["email"] = "angel@gmail.com"
# print(student)


# # 3.4 Updating Data
# # Definition:
# # An existing value can be changed by assigning a new value to its key.

# print("\n--- Updating Data ---")
# student["name"] = "Abin Sam"
# print(student)


# # 3.5 get()
# # Definition:
# # get() returns the value associated with a key.
# # If the key is missing, it returns None or a specified default value.

# print("\n--- get() ---")
# print(student.get("age"))
# print(student.get("mark"))
# print(student.get("mark", 20))


# # 3.6 update()
# # Definition:
# # update() adds new key-value pairs or updates existing values.

# print("\n--- update() ---")
# student.update({"age": 22})
# student.update({"department": "CS"})
# print(student)


# # 3.7 setdefault()
# # Definition:
# # setdefault() returns the existing value if the key exists.
# # Otherwise, it inserts the key with the specified default value.

# print("\n--- setdefault() ---")
# student.setdefault("age", 25)
# student.setdefault("hobbies", "Reading")
# print(student)


# # 3.8 pop()
# # Definition:
# # pop() removes the specified key and returns its value.

# print("\n--- pop() ---")
# student.pop("rno")
# print(student)


# # 3.9 popitem()
# # Definition:
# # popitem() removes and returns the last inserted key-value pair.

# print("\n--- popitem() ---")
# student.popitem()
# print(student)


# # 3.10 keys()
# # Definition:
# # keys() returns all the keys in a dictionary.

# print("\n--- keys() ---")
# print(student.keys())


# # 3.11 values()
# # Definition:
# # values() returns all the values in a dictionary.

# print("\n--- values() ---")
# print(student.values())


# # 3.12 items()
# # Definition:
# # items() returns all key-value pairs as tuples.

# print("\n--- items() ---")
# print(student.items())


# # 3.13 in Operator
# # Definition:
# # The in operator checks whether a key exists in a dictionary.
# # To check values, use the values() method.

# print("\n--- in Operator ---")
# print("name" in student)
# print("BCA" in student)
# print("BCA" in student.values())


# # 3.14 Dictionary For Loop - Keys
# # Definition:
# # A for loop can iterate through dictionary keys.

# print("\n--- Dictionary Keys ---")
# for key in student:
#     print(key)


# # 3.15 Dictionary For Loop - Values
# # Definition:
# # Values can be accessed using their keys inside a for loop.

# print("\n--- Dictionary Values ---")
# for key in student:
#     print(student[key])


# # 3.16 Dictionary items() with For Loop
# # Definition:
# # items() allows us to access keys and values together.

# print("\n--- Dictionary Key-Value Pairs ---")
# for key, value in student.items():
#     print(key, value)


# # ==========================================================
# # 4. STRING METHODS
# # ==========================================================

# # Definition:
# # A string is a sequence of characters.
# # String methods are used to perform operations on strings.


# # 4.1 split()
# # Definition:
# # split() divides a string into a list of substrings.

# print("\n--- split() ---")

# text = "Angel Aleena Anagha"
# names_list = text.split()
# print(names_list)


# # 4.2 split() with Separator
# # Definition:
# # split(separator) divides a string wherever the separator occurs.

# print("\n--- split() with Comma ---")

# text2 = "Angel,Aleena,Anagha"
# names_list2 = text2.split(",")
# print(names_list2)


# # ==========================================================
# # 5. PRINT FUNCTION - sep
# # ==========================================================

# # Definition:
# # sep is a print() parameter that specifies the separator
# # between multiple values. The default separator is a space.


# # 5.1 sep with Hyphen

# print("\n--- sep ---")
# print("Angel", "Aleena", "Anagha", sep="-")


# # 5.2 sep with Comma

# print(10, 20, 30, sep=",")


# # 5.3 sep with Space
# print("Python", "Full Stack", sep=" ")



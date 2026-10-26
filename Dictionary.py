
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



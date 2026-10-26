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
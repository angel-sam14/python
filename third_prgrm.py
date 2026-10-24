# CRUD OPERATIONS
# -----------------
# names=["Amal","Karthik"]
# while True:
#     choice = int(input("1. Add a name\n2.display names\n3.Edit a name\n4.Delete a name\n5.Exit\n Enter your choice:"))
#     match choice :
#         case 1:
#             name=input("Enter a name:")
#             names.append(name)
#         case 2:
#             print(format("sl.No.","<10"),format("Name"))
#             print('-'*25)
#             count = 1
#             for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#         case 3:
#              print(format("sl.No.","<10"),format("Name"))
#              print('-'*25)
#              count = 1
#              for x in names:
#                  print(format(count,"<10"),x)
#                  count+=1
#              edit_index= int(input("enter the Sl.No, of the name that you want to edit:"))-1
#              new_name=input("Enter the new name:")
#              names[edit_index] = new_name    
#         case 4:
#             print(format("sl.No.","<10"),format("Name"))
#             print('-'*25)
#             count = 1
#             for x in names:
#                 print(format(count,"<10"),x)
#                 count+=1
#             delete_index=int(input("Enter the Sl.No. of the name that you want to edit:"))-1
#             names.pop(delete_index)   
#         case 5:
#              break 
#         case _:
#             print('invalid entry')  

# ----------------------------------------------------------------------------------------------------------------------

# names = ["Amal", "Karthik"]

# while True:
#     choice = int(input(
#         "1. Add a name\n"
#         "2. Display names\n"
#         "3. Edit a name\n"
#         "4. Delete a name\n"
#         "5. Exit\n"
#         "Enter your choice: "
#     ))

#     match choice:
#         case 1:
#             name = input("Enter a name: ")
#             names.append(name)

#         case 2:
#             print(format("Sl.No.", "<10"), "Name")
#             print("-" * 25)
#             count = 1
#             for x in names:
#                 print(format(count, "<10"), x)
#                 count += 1

#         case 3:
#             print(format("Sl.No.", "<10"), "Name")
#             print("-" * 25)
#             count = 1
#             for x in names:
#                 print(format(count, "<10"), x)
#                 count += 1

#             edit_index = int(input(
#                 "Enter the Sl.No. of the name to edit: "
#             )) - 1

#             if 0 <= edit_index < len(names):
#                 new_name = input("Enter the new name: ")
#                 names[edit_index] = new_name
#             else:
#                 print("Invalid Sl.No.")

#         case 4:
#             print(format("Sl.No.", "<10"), "Name")
#             print("-" * 25)
#             count = 1
#             for x in names:
#                 print(format(count, "<10"), x)
#                 count += 1

#             delete_index = int(input(
#                 "Enter the Sl.No. of the name to delete: "
#             )) - 1

#             if 0 <= delete_index < len(names):
#                 names.pop(delete_index)
#             else:
#                 print("Invalid Sl.No.")

#         case 5:
#             break

#         case _:
#             print("Invalid entry")
# -------------------------------------------------------------------
# compact if statement

# number = 8
# if number % 2 == 0 :
#     print("Even")
# else:
#     print("odd")
# is_even_or_odd = "Even"  if number %2 == 0 else "odd" 
# print(is_even_or_odd)

# expression if condition else expression
# -------------------------------------------------------------------------------------------
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
t1=(4,5,6,7,8,9,4,4,5,6,4)
print(t1[4])

t2=4,5,6, 7,8                #----------->packing
print(type(t2))
a,b=(4,5)    # ----------->unpacking
print(a)
print(b) 
# functions in tuple
# -------------------- 
name1,name2 ="Abin","Angel"
print(t1.count(4))
print(t1.index(4))
print(t1.index(9))
print(len(t1))
for x in t1:
    print(x)
# l1 = List('Amal')   
    # -------------->['a','m','a','l']
# print(l1)
# l1[5]=19
t1=tuple('amal')
print(t1)

names=["angel","asdf","dfgh","dfgt"]
for index,name in enumerate(names):
    print(index,name)

print(" ".join(names)) 

# dictionary:key value pairs

student = {
    "name":"Angel",
    "age":21,
    "rno":3,
    "course":"BCA",
    "course":"BCOM"
}
items=student.items()
# print(student)
# print(type(student))
# print(student["age"])
student=["name"] = "Abin Sam"
print(student["name"])
student["email"] = "abinsam@gmail.com"
# print(student)
# print("BCA" in student)
# for x in student:
#     print(student[x])

print(student['age'])
print(student.get['age'])
print(student.get['agee'])
print(student.get['agee,20'])
student.update("hobbies":"writing","reading","dancing")
student.update("rno":4)
student.pop()
student.popitem()
student.values()
student.keys()


    
    
#  get:data edukkn
# update:data add akkn
#setdefault: existing data puthythayt update chym
# key illnki new add akkm
# allenki default value vrm
# pop:remove/delete chyn
# popitem:last item remove cheyyan
# values:values mathram display chyn(eg:('angel,21....))
# keys:only keys (eg:name,age........)
# items:separated ayt vrm(eg:()'name','angel'))


# enumerate:
# sep:
# split:list->string
# join:
# key:dictionary il ninn value access chyn
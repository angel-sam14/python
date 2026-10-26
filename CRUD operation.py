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
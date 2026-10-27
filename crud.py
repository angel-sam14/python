# # 23/10/26
# # --------

# students = [
#     {"id": 101, "name": "Angel", "department": "CS"},
#     {"id": 102, "name": "Aleena", "department": "CS"},
#     {"id": 103, "name": "Anagha", "department": "CS"}
# ]

# while True:
#     Choice = int(input("1. Add a student\n2. Display students\n3. Edit a student\n4. Delete a student\n5. Exit\nEnter your choice: "))

#     match Choice:
#         case 1:
#             name = input("Enter a name: ")
#             std_id = int(input("Enter the id: "))
#             department = input("Enter department: ")

#             students.append({"id": std_id, "name": name, "department": department})

#         case 2:
#             print(f"{'ID': ^6}{'Name': ^10}{'Department': ^12}")
#             print('-' * 28)

#             for student in students:
#                 print(f"{student['id']:<6}{student['name']:<10}{student['department']:<12}")

#             print('-' * 28)
#             print(f"Total count: {len(students)}")

#         case 3:
#             print(f"{'ID': ^6}{'Name': ^10}{'Department': ^12}")
#             print('-' * 28)

#             for student in students:
#                 print(f"{student['id']:<6}{student['name']:<10}{student['department']:<12}")

#             print('-' * 28)

#             id = int(input("Enter the id of the student that you want to edit: "))

#             edit_student = None

#             for student in students:
#                 if student['id'] == id:
#                     edit_student = student
#                     break

#             if edit_student:
#                 edit_student['name'] = input("Enter the new name: ")
#                 edit_student['department'] = input("Enter the new department: ")
#                 print("Student updated successfully!")
#             else:
#                 print("Student not found!")

#         case 4:
#             id = int(input("Enter the id of the student that you want to delete: "))

#             delete_student = None

#             for student in students:
#                 if student['id'] == id:
#                     delete_student = student
#                     break

#             if delete_student:
#                 students.remove(delete_student)
#                 print("Student deleted successfully!")
#             else:
#                 print("Student not found!")

#         case 5:
#             break

#         case _:
#             print("Invalid choice!")


#  -------------------------------------------------------------------------

# students = [
#     {"id": 101, "name": "Angel", "department": "CS"},
#     {"id": 102, "name": "Aleena", "department": "CS"},
#     {"id": 103, "name": "Anagha", "department": "CS"}
# ]
# while True:
#     Choice = int(input("1. Add a student\n2.Dispaly students\n3.Edit a student\n4.Delete a student\n5.Exit\nExit your choice:"))
#     match Choice:
#         case 1:
#              name = input("Enter a name:")
#              std_id = int(input("Enter the id:"))
#              department = input("Enter department:")
#              students.append({"id":std_id,"name":name,"department":department})
#         case 2 :
#             print(f"{'ID': ^6}{'Name': ^10}{'Department': ^12}")
#             print('-'*25)
#             for student in students:
#                 print(f"{student['id']:<4}{ student ['name']:<10}{student['department']:<10}")
#                 print('-'*25)
#                 print(f"Total count:{len(student): >7}")
#         case 3:
#             print(f"{"ID": ^4}{"Name": ^10}{"Department: ^10"}")
#             print('-'*25)
#             for student in students:
#                  print(f"{student['id']:<4}{ student ['name']:<10}{student['department']:<10}")
#             print('-'*25) 
#             id = int(input("Enter the id of the student that you want to edit:"))
#             edit_student = None
#             for student in students:
#                 if student['id'] == id:
#                     edit_student = student
#             edit_student['name'] = input("Enter the new name:")
#             edit_student['department'] = input("Enter the new department")      
#         case 5:
#             break
#         case _:
#             print('Invalid')
# ---------------------------------------------------------------------------------------------------------------


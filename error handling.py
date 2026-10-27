# 27/10/26
# ----------
#ERROR HANDLING
# ----------------
# exception:unindented
# types:
# SyntaxError
# RuntimeError:during runtime due to logical issues
# -----------------------------------------------------------
# 1. Nameerror:variable related error if not defined
# eg:
# print(x)

# 2. Typeerror:datatype related error(invalid type used in operation)
# eg:
# print(1 + '1')

# 3.ValueError:wrong type
# eg:
# n=int(input("Enter a number:"))

# 4. IndexError:index out of range
# eg
# l1 = [4,5,6]
# print(l1[5])

# 5. keyError:dicitionary key missing
# eg:
# student ={
#        "name":"Amal"
# }
# print(student['name'])

# 6. ZeroDivision:division by zero
# eg:print(10/0)

# 7. AttributeError
# eg:
# name="Amal"
# name.append()

# 8. FileNotFoundError-File does not exist
# eg:importError

# EXCEPTION HANDLING:unindented ayt olla error ine handle/fix chyn 
# try,except block ahn use chyne
# try:error varan chance olla code kodukkum
# except:error vannal nth chynm enn prnj kodkkm
# try :
    # code that may generate an error
    # pass
# except :
    # handles the error
    # pass
# else:
    # executes if no errors occur
    # pass
# finally:
    # used for memory cleanup
    # executes even if error occur or not
    # pass

# datatype class inte peru small letter aytum mattethoke pascal why?

# exception as e : eth type errror um handle chym

# try:
#     number1 = int(input("enter a first number:"))
#     number2 = int(input("enter a second number:"))
#     count = int(input("enter a count:"))
#     result = (number1+number2)/count
# except ZeroDivisionError:
#     print("input number should not be zero.")  
# except ValueError:
#     print("input must be an integer value.")
# else:
#     print(result)
# finally:
#     print("operation completed")
       
# try:
#     number = int(input("Enter a number:"))
#     print(100/number)
# except(ZeroDivisionError,ValueError):
#     print("Error occured")    

# try :
#     number = int(input("Enter a number:"))
#     print(100/number)
#     print(result)
# except Exception as e:
#     print("Error occured")    
# print("After the exception handling block")    

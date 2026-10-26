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

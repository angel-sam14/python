
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


# 23/10/26
# ---------

# Question 1: Student Marks

marks = []

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("Marks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

count = 0

for mark in marks:
    if mark > 50:
        count += 1

print("Students scored above 50:", count)


# Question 2: Even and Odd Numbers

numbers = []
even = []
odd = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Numbers:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)


# Question 3: Positive, Negative and Zero

positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input("Enter number: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)


# Question 4: Search an Element

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

search = int(input("Enter number to search: "))

if search in numbers:
    print("Number found")
    print("Position:", numbers.index(search) + 1)
else:
    print("Number not found")


 # Question 5: Shopping Cart

prices = []

n = int(input("Enter number of products: "))

for i in range(n):
    price = float(input("Enter product price: "))
    prices.append(price)

total = sum(prices)

print("Total amount:", total)

if total > 5000:
    discount = total * 0.10
    final_amount = total - discount
else:
    discount = 0
    final_amount = total

print("Discount:", discount)
print("Final amount:", final_amount)


# Question 6: Number Analyzer

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Even count:", even)
print("Odd count:", odd)


# Question 7: Remove Negative Numbers

numbers = []
positive = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for num in numbers:
    if num > 0:
        positive.append(num)

print("Original list:", numbers)
print("Positive numbers:", positive)


# Question 8: Find Duplicate Values

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Numbers:", numbers)
print("Duplicate numbers:", duplicates)


# Question 9: Palindrome Number

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


    # Question 10: Armstrong Number

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# Question 11: Prime Number

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")


# Question 12: Largest Digit

num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)  



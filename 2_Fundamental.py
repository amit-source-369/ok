# 1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%

# salary = int(input("Write down your salary : "))
# if (salary < 30000):
#     print("Your Final Fixed rate is : ", salary * 5 / 100)
# elif(salary > 30000 and salary < 70000):
#     print("Your Final Fixed rate is : ", salary * 15 / 100)
# else:
#     print("Your Final Fixed rate is : ", salary * 25 / 100)

# 2. Write a function that takes two integers a and b prints all even numbers between them (inclusive).

# def even(a, b):
#     for i in range(a, b+1, 1):
#         if (i % 2 == 0):
#             print(i)        

# a = int(input("Write any value : "))
# b = int(input("Write any value : "))
# even(a, b)

# 3. Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]

# n = int(input("Enter any number : "))

# def get_num(n):
#     while n > 0:
#         Num = n % 10
#         print(Num)
#         n = int(n / 10)

# get_num(n)

# 4. Write a function to return the count the number of digits in a number, n

# n = int(input("enter your number : "))
# def count_num(num):
#     count = 0
#     while num>0:
#         count += 1
#         num = num // 10
#     return count

# print(count_num(n))

# 5. Write a function to return the sum of digits of a number, n .

# n = int(input("Enter any number : "))
# def sum_n(num):
#     sum=0
#     while num > 0:
#         digit = num % 10
#         sum += digit
#         num = num // 10
#     return sum

# print(sum_n(n))

# 6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

# for i in range(1, 101):
#     if (i%3==0 and i%5==0):
#         print(i)

# 7. Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”

# while True:
#     n = input("Enter any Positive or Negative Value and 'Quit' for exit : ")
#     if (n == "Quit"):
#         break
#     print("Negative") if (int(n) < 0) else print("Positive")

# 8.  Let’s create a Simple Calculator that performs arithmetic operations. 
# Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.
# [ operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’ ]

# def calculator(a, b, operation):
#     if (operation == '+'):
#         print(a + b)
#     elif (operation == '-'):
#         print(a - b)
#     elif (operation == '*'):
#             print(a * b)
#     elif (operation == '/'):
#             print(a / b)

# a = int(input("Enter 1st Value : "))
# b = int(input("Enter 2nd Value : "))
# operation = input("Enter Operator : ")
# calculator(a, b, operation)

# 9. Write a function is_prime(n) that returns True if is a prime number and False otherwise, using a loop.

# num = int(input("Check your number is Prime or not : "))

# def is_prime(n):
#     is_true = False
#     for i in range(2, n-1):
#         if (n%i == 0):
#             is_true = True
#             break
#         else:
#             is_true = False

#     return is_true
    

# print(is_prime(num))

# 10. Let’s create a “Number Guessing Game”. 
# Given a secret number (already decided by you), write a program that asks the user to guess it and prints:
# • "Too high" if the guess is above the number
# • "Too low" if the guess is below
# • "Correct!" if the guess matches

target = 10

while True:
    guess = int(input("Guess the number : "))
    if guess == 'q':
        break
    if target > guess:
        print("Too Low -> Go Higher")
    elif target < guess:
        print("Too high -> Come lower")
    elif target == guess:
        print("Correct Congrets! your Target number is : ", target)
        break
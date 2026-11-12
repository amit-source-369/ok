# Q.1 -> Write a program that asks the user for their name and age, then prints a sentence like:

# name = input("Your name : ")
# age = input("Your Age : ")
# print(f"Hello {name}, you are {age} years old!")

# Q.2 -> Take two numbers as input from the user and print their sum, difference, product, and quotient

# a = float(input("Your 1st Number : "))
# b = float(input("Your 2nd Number : "))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# Q.3 -> Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# a = float(input("Your 1st Number : "))
# b = float(input("Your 2nd Number : "))
# c = float(input("Your 3rd Number with decimals : "))
# print((a+b+c)/3)

# Q.4 -> The user enters a string containing a number (e.g., "45"). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

# text = input("Enter your age : ")
# int_text = int(text)
# float_text = float(text)
# str_text = str(text)
# print(f"{int_text} and type is {type(int_text)}")
# print(f"{float_text} and type is {type(float_text)}")
# print(f"{str_text} and type is {type(str_text)}")

# Q.5 -> Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2
# Based on what you learnt in the lecture explain why the output is what it is.

# x = 10 + 3 * 2 ** 2
# print(x)

# Q.6 -> Write a program to swap values of two numbers entered by the user.

# a = float(input("Your 1st Number : "))
# b = float(input("Your 2nd Number : "))
# print(f"Before swap : a - {a} and b - {b}")
# c = a
# a = b
# b = c
# print(f"After swap : a - {a} and b - {b}")

# Q.7 -> Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit.
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

# CelsiusTemp = float(input("Enter your temperature in celsius : "))
# FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
# print(f"Your temperature in celsius {CelsiusTemp} to fahrenheit is {FahrenheitTemp}")

# Q.8 -> Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r**2 (value of π = 3.14)

# rad = float(input("Enter radius : "))
# Area = 3.14 * rad**2
# print(f"Area is {Area}")

# Q.9 -> Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest:
# SI = (P ∗ R ∗ T )/100

# p = float(input("Enter principle : "))
# r = float(input("Enter rate : "))
# t = float(input("Enter time : "))
# print((p*r*t)/100)

# Q.10 -> Take a decimal number as input (like 45.78) and output its:
# • integer part - 45
# • fractional part - .78

# a = float(input("Your Number in decimal : "))
# int_a = int(a)
# float_a = a % int_a
# print(f"Int value is {int_a}, Fractional value is {float_a}")

print("ok")
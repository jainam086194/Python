#!/usr/bin/python3
import math
import re


# print("Hello world")

# program to print pythagorian triplets

# n = int(input("Enter maximum number: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         # sqrt_num = math.sqrt(i**2 + j**2)
#         if (sqrt_num:=math.sqrt(i**2 + j**2)) == int(sqrt_num):
#             print(i, j, int(sqrt_num))

# n = int(input("Please give a number: "))
# square= n ** 2
# if square: > 3:
#     print("The number is greater than 3.")
#     print(f"The square of {n} is {square}.")

# def f(x):
#     return x + 4

# numbers = [3, 7, 2, 9, 12]

# odd_numbers = [result for x in numbers if (result := f(x) % 2)]
# print(odd_numbers)


# odd_numbers = [result for x in numbers if (result := f(x)) % 2]
# print(odd_numbers)


# txt = """The Python training course started at 2022-02-4 
# the other one at 2022-01-24
# only one date per line, if at all
# the dates may also be in this format 2020/10/15
# or 20-10-04"""

# for line in txt.split('\n'):
#     date = re.search(r'(\d{2,4})[-/](\d{2})[-/](\d{2})', line)
    
    
# with open('training_course_info.txt') as fh:
#     data = fh.read(52)
#     if data:
#         print(data.rstrip())
#         data = fh.read(52)

# word_to_find = "Advanced"
# with open("training_course_info.txt") as file:
#     while (line := file.readline()):
#         if word_to_find in line:
#             print(line)

# import random

# lower_bound, upper_bound = 1, 20
# to_be_guessed = random.randint(lower_bound, upper_bound)
# guess = 0
# while guess != to_be_guessed:
#     guess = int(input("New number: "))
#     if guess > to_be_guessed:
#         print("Number too large")
#     elif guess < to_be_guessed:
#         print("Number too small")


# import random
# guess = random.randint(1, 10)
# print(f"guess is {guess}")

# try:
#     while guess != (to_be_guessed := int(input("Enter number: between 1 and 10: "))):
#         if to_be_guessed > 10 or to_be_guessed < 1:
#             print("Enter number between 1 and 10 only!")
#         elif guess < to_be_guessed:
#             print("Your guessed number is greater than actual number")
#         elif guess > to_be_guessed:
#             print("Your guessed number is less than actual number")
#         else:
#             print("Wrong Input!!")
#     else:    
#         print("Congratulation! You won!")
# except:
#     print("Invalid Input!!!! Try again")

# x, y = 3, 4
# y,x=x,y
# print(x,y)


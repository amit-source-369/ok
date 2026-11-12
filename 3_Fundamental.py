# 1. Ask the user for a string and check whether it is a palindrome or not. 
# A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.

# string = input("Enter a word to check pallindrome or not : ")
# reverse = ""
# for ch in string:
#     reverse = ch + reverse

# if (string == reverse):
#     print("Pallindrome")
# else:
#     print("Not a pallindrome")

# 2. Given a list of integers compute the average of all numbers in the list.

# integer = [1, 2, 3, 4, 5]
# sum = 0
# for i in integer:
#     sum += i

# avg = sum/len(integer)
# print(avg)

# 3. Input two lists of integers from the user. Merge them into one list and sort the result.

# list_one = list(map(int, input("Enter a list of integer : ").split()))
# list_two = list(map(int, input("Enter a list of integer : ").split()))

# merge_list = list(set(list_one + list_two))
# merge_list.sort()
# print(merge_list)

# 4. Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

# integer = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tup_even = ()
# tup_odd = ()

# for i in integer:
#     if (i % 2 == 0):
#         tup_even += (i, )
#     else:
#         tup_odd += (i, )
# print(tup_even)
# print(tup_odd)

# 5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

# student_marks = {
#     "amit": 99,
#     "pankaj": 76,
#     "suresh": 93,
#     "mahesh": 56,
#     "rajesh": 56,
#     "suraj": 67
# }

# print("==============Operation on student table=================")

# user_input = input("Enter 'A' for Add a student, 'B' for Update marks, 'C' for Search for student, 'D' for Display all : ").upper()

# if (user_input == 'A'):
#     name = input("Enter student name : ")
#     marks = input("Enter student marks : ")
#     student_marks[name] = marks
#     print(student_marks)
#     print("Entry Added")
# elif (user_input == 'B'):
#     name = input("Enter student name : ")
#     marks = input("Enter updated marks : ")
#     student_marks.update({name: marks})
#     print(student_marks)
#     print("Entry Updated")
# elif (user_input == 'C'):
#     student_name = input("Enter student name : ")
#     for name, marks in student_marks.items():
#         if (student_name == name):
#             print(f"Student name is {name}: Marks is {marks}")
#             break
#     print("User Result Displayed")
# else:
#     for name, marks in student_marks.items():
#         print(f"{name} => {marks}")

# 6. Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example: {"apple": 5, "banana": 6, "kiwi": 4, ...}

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# word_dict = {}

# for w in words:
#     word_dict.update({w: len(w)})
# print(word_dict)

# 7. Write a program that takes a string from the user and prints the number of spaces in the string.

# user_string = input("Write any line : ")
# count=0
# for s in user_string:
#     if s == " ":
#         count+=1
# print(f"Number of spaces in a string {user_string} is {count}")

# 8. Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
# [Hint - use sets]

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 3]
# set_l1 = set(list1)
# set_l2 = set(list2)
# common_finder = set_l1.intersection(set_l2)
# if common_finder == set():
#     print(set_l1.intersection(set_l2))
#     print("No common element")
# else:
#     print("Common element found")
#     print(set_l1.intersection(set_l2))

# 9. Given a list, print all elements that appear more than once in the list.
# whole_list = [4, 2, 6, 3, 5, 4, 2, 1, 2, 7, 9, 8, 6, 4]
# whole_list = [1, 3, 2, 3, 4, 3, 2, 4, 1, 5, 7, 8]
# seen_set = set()
# duplicate_set = set()
# for num in whole_list:
#     if num in seen_set:
#         duplicate_set.add(num)
#     else:
#         seen_set.add(num)
# print(duplicate_set)

# Ask the user for a string and print:
# • All unique characters
# • The count of unique characters

input_string = input("Enter any string : ")
unique = set()
for ch in input_string:
    if ch not in unique:
        unique.add(ch)

print(f"Unique char in string '{input_string}' is {unique}")
print(f"Count = {len(unique)}")
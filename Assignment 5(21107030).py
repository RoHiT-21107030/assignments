# Q1
# statement = input("Enter a statement:")
# # creating empty string
# reverse = ""
# # taking alphabets from the string one by one and adding them to make a new variable with the string reversed.
# for alphabet in statement:
#     reverse = alphabet + reverse
# # printing the new variable containing the reversed string.
# print(reverse)

# Q2
# # enter the upper and lower limit of the range
# Lower_limit = int(input("Enter a lower limit for the range:"))
# Upper_limit = int(input("Enter an upper limit for the range:"))
# # enter a number to check divisibility with
# num_input = int(input("Enter a number for checking multiples:"))
# # taking number one by one from the range and checking its divisibility
# for number in range(Lower_limit, Upper_limit):
#     if number % num_input == 0:
#         # printing the number if it is divisible
#         print(limit)
#     else:
#         continue

# Q3
num_1 = int(input("Enter the length of First side: "))
num_2 = int(input("Enter the length of Second side: "))
num_3 = int(input("Enter the length of Third side: "))

semi_perimeter=(num_1+num_2+num_3)/2

Area = ((semi_perimeter)*(semi_perimeter-num_1)*(semi_perimeter-num_2)*(semi_perimeter-num_3))**(0.5)

# if (num_1+num_2 <= num_3) or (num_2+num_3 <= num_1) or (num_3+num_1 <= num_2):
conditions_1 = [num_1+num_2 <= num_3, num_2+num_3 <= num_1, num_3+num_1 <= num_2]
conditions_2 = [num_1 + num_2 > num_3, num_2 + num_3 > num_1, num_3 + num_1 > num_2]
for condition_1 in conditions_1 and condition_2 in conditions_2:
    if condition_1 is True:
        print("No")
        check = 0

    elif conditio_2 is True:
        # if (num_1+num_2 > num_3) and (num_2+num_3 > num_1) and (num_3+num_1 > num_2):
        # conditions_2 = [num_1 + num_2 > num_3, num_2 + num_3 > num_1, num_3 + num_1 > num_2]
        # for condition_2 in conditions_2:
        # if condition_2 is True:
        check = 1
        print("Yes")

        if check == 1:
            print("Area of triangle is ", Area)
        else:
            print("invalid triangle ")

# # if (num_1+num_2 > num_3) and (num_2+num_3 > num_1) and (num_3+num_1 > num_2):
# conditions_2 = [num_1+num_2 > num_3, num_2+num_3 > num_1, num_3+num_1 > num_2]
# for condition_2 in conditions_2:
#     if condition_2 is True:
#         check = 1
#         print("Yes")
#
# if check == 1:
#     print("Area of triangle is ", Area)
# else:
#     print("invalid triangle ")

# # Q4
# n = 5
# for i in range(1, n):
#     print("*"*i)
# for i in range(n, 0, -1):
#     print("*" * i)

# Q5
# num_rows = int(input("Enter the number of rows to be formed:"))
# Characters = ["A","B","C","D","E",'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
# for i in range(1, num_rows+1):
#     for letter in Characters:
#         print(letter)
#
#

#
# # Q6
# #Taking upper and lower limit
# Lower_limit = int(input("Insert lower limit of the range: "))
# Upper_limit = int(input("Enter the upper limit of the range: "))
#
# print("Prime numbers between", Lower_limit, "and", Upper_limit, "are:")
#
# for number in range(Lower_limit, Upper_limit + 1):
#    # all prime numbers are greater than 1
#    if number > 1:
#        for i in range(2, number):
#            if (number % i) == 0:
#                break
#        else:
#            print(number)
#
# # Q7
# # Checking multiples if 7 and divisibility by 11
# for i in range(0, 500):
#     if i % 7 == 0 and i % 11 == 0:
#         print(i)
#     else:
#         continue
#
# # Q8
#
# Creating blank list
# list_1 = []
# # Taking 10 values from user
# for i in range(10):
#     list_1.append(int(input("Enter a number: ")))
#
# print(list_1)
#
# print('''
#       Press 1 for positive numbers
#       Press 2 for negative numbers
#       Press 3 for odd numbers
#       Press 4 for even numbers
#       Press 5 for checking frequency of numbers ''', "\n")
#
# operation = int(input("Please choose an operation: "))
#
# if operation == 1:
#     for j in list_1:
#         if j > 0:
#             print(j)
# elif operation == 2:
#     for j in list_1:
#         if j < 0:
#             print(j)
# elif operation == 3:
#     # Checking for odd numbers
#     for j in list_1:
#         if j % 2 != 0:
#             print(j)
# elif operation == 4:
#     # Checking for even numbers
#     for j in list_1:
#         if j % 2 == 0:
#             print(j)
# elif operation == 5:
#     # Converting list to dictionary and using count
#     dict_1 = {num: list_1.count(num) for num in list_1}
#     print(dict_1)

# Q9
# Creating empty list
# list_2 = []
# # Taking 10 inputs from user and then adding them to list
# for i in range(10):
#     list_2.append(input("Enter word: "))
# print(list_2)
# # Converting list to dictionary and then using count
# dict_2={word:list_2.count(word) for word in list_2}
#
# print(dict_2)
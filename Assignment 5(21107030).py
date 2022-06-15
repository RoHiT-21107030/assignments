# Q1
statement = input("Enter a statement:")
# creating empty string
reverse = ""
# taking alphabets from the string one by one and adding them to make a new variable with the string reversed.
for alphabet in statement:
    reverse = alphabet + reverse
# printing the new variable containing the reversed string.
 print(reverse)

# Q2
# enter the upper and lower limit of the range
Lower_limit = int(input("Enter a lower limit for the range:"))
Upper_limit = int(input("Enter an upper limit for the range:"))
# enter a number to check divisibility with
num_input = int(input("Enter a number for checking multiples:"))
# taking number one by one from the range and checking its divisibility
for number in range(Lower_limit, Upper_limit):
    if number % num_input == 0:
        # printing the number if it is divisible
        print(limit)
    else:
        continue

# Q3
# Taking user input
num1 = int(input("Enter the length of first side: "))
num2 = int(input("Enter the length of second side: "))
num3 = int(input("Enter the length of third side: "))
# Calculating semi-perimeter
semi_pem = (num1+num2+num3)/2
# Calculating Area
Area = ((semi_pem)*(semi_pem-num1)*(semi_pem-num2)*(semi_pem-num3))**(0.5)
# Checking conditions
if (num1+num2 <= num3) or (num2+num3 <= num1) or (num3+num1 <= num2):
    print("The triangle is not possible.")
    check = 0

if (num1+num2 > num3) and (num2+num3 > num1) and (num3+num1 > num2):
    check = 1
    print("The triangle is possible.")

if check == 1:
    print("Area of triangle is ", Area)
else:
    print("invalid triangle ")

 # Q4
n = 5
# first printing the stars of the upper half figur in increment
for i in range(1, n):
    print("*"*i)
# then print the lower half stars in decrement
for i in range(n, 0, -1):
    print("*" * i)

# Q5
# Taking user input
row_num = int(input("Enter the number of rows: "))
i = 0 # Making a variable to repeat the alphabets
a = 0 # Will be used for incrementation of chr function to make the next alphabet
line = 1 #variable denoting the nth line
for x in range(row_num): 
    i = 0
    while i < line:
        print(chr(65 + a), end = "")# printing the alphabet
        i = i + 1 # for printing new alphabet
        a = a + 1 # for new alphabet
    print("") # for new line
    line = line + 1  # line increment
              
# Q6
#Taking upper and lower limit
Lower_limit = int(input("Insert lower limit of the range: "))
Upper_limit = int(input("Enter the upper limit of the range: "))

print("Prime numbers between", Lower_limit, "and", Upper_limit, "are:")

for number in range(Lower_limit, Upper_limit + 1):
   # all prime numbers are greater than 1
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)

# Q7
# Checking multiples if 7 and divisibility by 11
for i in range(0, 500):
    if i % 7 == 0 and i % 11 == 0:
        # Printing the numbers divisible by both 7 and 11
        print(i)
    else:
        continue

# Q8

Creating blank list
list_1 = []
# Taking 10 values from user
for i in range(10):
    list_1.append(int(input("Enter a number: ")))

print(list_1)

print('''
      Press 1 for positive numbers
      Press 2 for negative numbers
      Press 3 for odd numbers
      Press 4 for even numbers
      Press 5 for checking frequency of numbers ''', "\n")

operation = int(input("Please choose an operation: "))

if operation == 1:
    # Checking for positive numbers
    for j in list_1:
        if j > 0:
            print(j)
elif operation == 2:
    # Checking for negative numbers
    for j in list_1:
        if j < 0:
            print(j)
elif operation == 3:
    # Checking for odd numbers
    for j in list_1:
        if j % 2 != 0:
            print(j)
elif operation == 4:
    # Checking for even numbers
    for j in list_1:
        if j % 2 == 0:
            print(j)
elif operation == 5:
    # Converting list to dictionary and using count
    dict_1 = {num: list_1.count(num) for num in list_1}
    print(dict_1)

# Q9
Creating empty list
list_2 = []
# Taking 10 inputs from user and then adding them to list
for i in range(10):
    list_2.append(input("Enter a word: "))
print(list_2)
# Converting list to dictionary and then using count
dict_2={word:list_2.count(word) for word in list_2}

print(dict_2)

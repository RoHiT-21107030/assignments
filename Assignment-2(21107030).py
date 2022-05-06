# Q1
given_string = "Python is a case sensitive language"
# Find Length
print(len(given_string))

# Reversing order
print(given_string[::-1])

# Slicing
new_string = given_string[10:26]
print(new_string)

# Replacing String
print(given_string.replace('a case sensitive', 'object oriented'))

# Finding the index of "a"
print(given_string.find("a"))

# Removing the blank spaces
print(given_string.replace(' ', ''))


# Q2
# Taking Input
Name = input("Enter your name: ")
SID = input("Enter your SID: ")
Dep_name = input("Enter your department name: ")
CGPA = input("Enter your CGPA: ")

# Output to be printed
print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", Dep_name, "department and my CGPA is", CGPA)

# Q3
a = 56
b = 10
print("a&b=", a & b)
print("a|b=", a | b)
print("a^b", a ^ b)
print("a << 2 : ", a << 2, " and b << 2: ", b << 2)
print("a >> 2 :", a >> 2, " and b >> 4:", b >> 4)


# q4
input_sent = input("Enter a sentence:")
if "name" in input_sent:
    print("Yes")

else:
    print("No")

# Q5
# Taking input value of the sides
side_1 = int(input("Enter the side 1: "))
side_2 = int(input("Enter the side 2: "))
side_3 = int(input("Enter the side 3: "))

a = side_1 + side_2
b = side_2 + side_3
c = side_3 + side_1

x = (side_1 < b)
y = (side_2 < c)
z = (side_3 < a)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)

# Q6
# Obtaining user input
a = int(input("enter the number a: "))
b = int(input("enter the number b: "))

# Using binary XOR operation and then conversion to string
c = str(bin(a ^ b))

print(c.count("1"))




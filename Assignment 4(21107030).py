# Q1
choice = 'y'
while choice == 'y':
    marks = float(input("Enter marks acquired: "))
    if marks < 25:
        print("Your Grade is F")
    elif marks >= 25 and marks < 45:
        print("Your Grade is E")
    elif marks >= 45 and marks < 50:
        print("Your Grade is D")
    elif marks >= 50 and marks < 60:
        print("Your Grade is C")
    elif marks >= 60 and marks < 80:
        print("Your Grade is B")
    elif marks >= 80 and marks <= 100:
        print("Your Grade is A")
    elif marks > 100:
        print("Please enter marks correctly.")

    choice = input("press 'y' to continue\n")

# Q2
choice = 'y'
while(choice =='y'):
    year = int(input("Enter a year:"))
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print(year, "is not a leap year.")

    elif year % 4 == 0:
        print(year, "is a leap year.")

    else:
        print(year, "is not a leap year.")

    choice = input("press 'y' to continue\n")


# Q3
n = 10
while(n>0):
    n = n-1
    import random

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num1 = random.choice(a)
    num2 = random.choice(a)
    print(num1, "x", num2)
    answer = int(input("Enter the correct answer:\n"))
    if answer is num1*num2:
        print("Correct")
    elif answer is not num1*num2:
        print("Wrong!, the correct answer is ", num1*num2)
    print("Number of tries left:", n)

print("Thank you for playing the game.")

# Q4
for candies in range(0, 200):
    if candies % 5 == 2 and candies % 6 == 3 and candies % 7 == 2:
        print("If the candy is divided evenly among 5 people, there will be 2 leftover candies")
        print("If the candy is divided evenly among 6 people, there will be 3 leftover candies")
        print("If the candy is divided evenly among 7 people, there will be 2 leftover candies")
        print("The amount of candies are", candies)

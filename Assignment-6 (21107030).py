# Q1
user_input = int(input("Enter a number:"))
sum_of_the_divisor = 0
for i in range(1 ,user_input):
    if (user_input%i==0):
        sum_of_the_divisor += i
        if sum_of_the_divisor==user_input:
            print("Yes, It is a perfect number.")
            break

else:
    print("No, It is not a perfect number.")

# Q2
user_input = str(input("Enter a word, phrase or sequence: "))
user_input1 = user_input.replace(" ", "")
palindrome = user_input1[::-1]
if user_input1 == palindrome :
  print("Input is a palindrome.")
else:
  print("Input is not a palindrome.")

# Q3
user_input = int(input("Enter the number of rows of pascal triangle:"))
list1 = [1]
list2 = [0]
print(list1)
for i in range(0, user_input):

    list1 = [l+r for l,r in zip(list1+list2, list2+list1)]
    print(list1)

# Q4
user_input = str(input("Enter a word or sentence: "))
user_input1 = user_input.lower()
alphabets = "qwertyuiopasdfghjklzxcvbnm"
for char in alphabets :
  if char not in user_input1 :
    print("No, It is NOT a Pangram.")
    break
else:
    print("Yes, It is a Pangram.")

# Q5
user_input = input("Enter words with hyphen(For example:green-red-yellow-black-white):")
user_input1 = user_input.lower()
input_split = user_input1.split("-")
input_split.sort()
print("-".join(input_split))

# Q6
def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Rohit","Mechanical",21107030)

# Q7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

# Q8
def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
	if (found == False):
		print(" not exist ")


arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)

# Q9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")

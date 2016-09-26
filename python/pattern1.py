import math
import re

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line

print("######################################### Ex 1 ###################################\n")

result = []
for i in range (2000, 3000):
    if (i % 5) and not (i % 7):
       result.append(str(i))

print(','.join(result))

#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

print("######################################### Ex 2 ###################################\n")

C=50
H=30
D = input('value of D ?')
items = D.split(',')
result = []
def f(d):
	return str(round(math.sqrt(2 * C * d / H)))

for i in items:
   result.append(f(int(i)))

print(','.join(result))


#Question:
#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At l1east 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1

print("######################################### Ex 3 ###################################\n")

P = input('Input a list of passwords ?')
items = P.split(',')

def validate(x):
    pattern1="[A-Za-z]"
    pattern2="[0-9]"
    pattern3="[$#@]"

    if (len(x) < 6) or (len(x) > 12):
	    return 0
    if re.search(pattern1,x) and re.search(pattern2,x) and re.search(pattern3,x):
        return 1
    else:
        return 0

for i in items:
   if (validate(i)):
      print(i)
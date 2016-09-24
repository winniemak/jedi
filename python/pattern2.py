'''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2 dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
''' 

result = []
sub_result = []
x,y = input("Input 2 digits X and Y ").split(',')
print(x,y)
for i in range(int(x)):
   for j in range(int(y)):
       sub_result.append(str(i*j))   
   result.append(sub_result)
   sub_result=[]
   
print(result)
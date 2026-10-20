	
import math

#Assignment 1 No1
print("Assignment1 No1")
x,y = 4,5
print("Before swapping: ",x,y)
x,y = y,x
print("After swapping: ",x,y)

#Assignment 1 No2
print("Assignment1 No2")
a=10
b=20
c=30
sum=a+b+c
print("Sum of two digits: ",sum)

#Assignment 1 No3
print("Assignment1 No3")
num=int(input("Enter Number"))
if num%2 == 0 :
  print(num ," is even.")
else: 
  print(num,"is odd")

#Assignment 1 No4
print("Assignment1 No4")
answer="no"
while answer == "no" :
 mark = int(input("Please enter your marks"))
 print(mark)
 print(type(mark))
 if mark >= 76 :
  print(mark,"is Distinarion")
  answer=input("Do you want end program yes/no?")
 elif mark >= 54:
  print(mark,"is second class")
  answer=input("Do you want end program yes/no?")
 elif mark >=41:
  print(mark,"is pass class")
  answer=input("Do you want end program yes/no?")
 else:
  print("Fail")
  answer=input("Do you want end program yes/no?")
 

 #Assignment 1 N05
 print("Assignment1 No5")
num=int(input("Enter number"))
res = math.factorial(num)
print(num,"Factorial is",res)

#Assignmern 1 No6
print("Assignment1 No6")
num=int(input("Enter number"))
if(num==2):
   print(num,"is prime number")
elif num%2 == 0 :
 print (num,"is not prime number")
else:
 print(num,"is prime number")


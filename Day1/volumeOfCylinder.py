import math


pi = 3.14
radius = float(input("Enter your radius"))
height = float(input("Enter your height"))
volume = pi*(math.sqrt(radius))*height
print("Volume of Cylinder is ", volume)

pi=3.14
radius = float(input("Enter radius"))
height = float (input ("Enter Height"))
volume = pi*(math.pow(radius,2))*height
r="%*.*f"%(5,3,volume)
print("Volume of Cylinder is " , r)


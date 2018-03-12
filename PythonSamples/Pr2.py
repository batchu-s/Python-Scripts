#!/usr/bin/python36
import math as M

radius=float(input("Enter the radius of the circle: "))
print(type(radius))
area=M.pi*radius*radius
perimeter=2*M.pi*radius

print("The area of the circle is:",area)
print("The perimeter of the circle is:",perimeter)


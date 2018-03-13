#!/usr/bin/python36
import math as m

print("Enter a three digit number: ")
num=int(input())

if num<100 or num>999:
    print("######Not a three digit number######")
    exit()

d1=int(num/100)
d2=int(num%100/10)
d3=int(num%10)

sum=m.pow(d1,3) + m.pow(d2,3) + m.pow(d3,3)
print(sum)


if num == sum:
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number")


#!/usr/bin/python36

print("Enter the year in <YYYY> format: ",end='')
year=int(input())

if year%100 == 0 or year%400 == 0:
    print(year," is a leap year")
elif year%4 == 0:
    print(year," is a leap year")
else:
    print(year," is not a leap year")


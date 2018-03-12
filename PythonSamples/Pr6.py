#!/usr/bin/python36

student_name=input("Enter the student name: ")
student_id=input("Enter student id: ")
print("Enter the marks of three subjects: ")
s1=int(input())
s2=int(input())
s3=int(input())
grade=''
if s1<0 or s1>100 or s2<0 or s2>100 or s3<0 or s3>100:
    print("Invalid marks")
    exit()

total=s1+s2+s3
avg=total/3.0

if s1<40 or s2<40 or s3<40:
    grade='fail'
elif avg>=80:
    grade='honours'
elif avg>=70:
    grade='distinction'
elif avg>=60:
    grade='first class'
elif avg>=50:
    grade='second class'
else:
    grade='pass'

print("Student id: ",student_id)
print("Student name: ",student_name)
print("Grade: ",grade)


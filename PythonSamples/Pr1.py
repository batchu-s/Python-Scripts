#!/usr/bin/python36

print("Enter any four numbers:")
p=input()
q=input()
r=input()
s=input()

if p>q and p>r and p>s:
    print("The largest number is:",p)
elif q>r and q>s:
     print("The largest number is:",q)
elif r>s:
    print("The largest number is:",r)
else:
    print("the largest number is:",s)


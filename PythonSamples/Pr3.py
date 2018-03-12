#!/usr/bin/python36
while True:
    print("Enter '0' to exit")
    ch=input("Enter any character:")
    if ch=='0':
        exit()
    else:   
        if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            print("It is an alphabet")
        else:
            print("It is not an alphabet")


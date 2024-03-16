#write a program to accept your one single sub marks from user and check if marks >35 print cheated if marks==35 pass if marks <35 fail
a=float(input("enter maths marks:"))
if a>35:
    print("cheated")
elif a==35:
    print("pass")
else:
    print("fail")

#write a program in which you take an integer input from user if that integer if itis divisible by 3 and 6 print good number is the integer is divisible by 2 and 7 print an average number
#if the integer is divisible by 4 or 9 then print awesome number else print bad.
a=int(input("enter a number:"))
if a%3==0 and a%6==0:
    print("good number")
elif a%2==0 and a%7==0:
    print("average number")
elif a%4==0 or a%9==0:
    print("awesome number")
else:
    print("bad number")

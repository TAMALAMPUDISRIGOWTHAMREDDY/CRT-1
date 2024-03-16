#take an integer as input from the user and check whether if the number is divisible by sum of digits or not
a=int(input())
temp=a
sum=0
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
if temp%sum==0:
    print("divisible")
else:
    print("not")

n=int(input())
temp=n
res=0
while n>0:
    b=n%10
    res=res*10+b
    n=n//10
if res==temp:
    print("palindrome")
else:
    print("not palindrome")

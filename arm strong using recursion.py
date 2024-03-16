def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
a=count(153)
def arm(n):
    if n==0:
        return 0
    
    return ((n%10)**a)+arm(n//10)
b=arm(153)
print(b)
if 153==arm(153):
    print("yes")
else:
    print("no")

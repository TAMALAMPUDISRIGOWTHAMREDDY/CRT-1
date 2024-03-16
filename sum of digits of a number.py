#write a recursive fun to calculate sum of digits of a number
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
a=sum(15)
print(a)

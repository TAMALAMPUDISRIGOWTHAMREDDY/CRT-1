n=int(1578)
n1=n
count=0
sum=0
while n>0:
    n=n//10
    count=count+1
while n1>0:
    b=n1%10
    sum=sum+b**count
    count=count-1
    n1=n1//10
print(sum)

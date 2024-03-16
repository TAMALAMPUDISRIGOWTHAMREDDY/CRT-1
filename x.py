a=int(input())
b=a
sum=0
i=1
while a>0:
    if a%i==0:
        sum=sum+i
    i=i+1
print(sum)
if b>sum:
    print("yes")
else:
    print("no")

n=154
temp=n
sum=0
count=0
while temp>0:
    temp=temp//10
    count+=1
temp=153
while n>0:
    b=n%10
    sum=sum+b**count
    n=n//10
print(sum)
if temp==sum:
    print("armstrong")
else:
    print("not")
    
    

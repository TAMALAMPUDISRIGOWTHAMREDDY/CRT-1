#take a number input from user check if the sum  of factors of that numberis greater than original number or not
a=int(input())
b=a
sum=0
for i in range (1,a//2+1):
    if a%i==0:
        sum=sum+i
print(sum)
if sum>b:
    print("yes")
else:
    print("no")

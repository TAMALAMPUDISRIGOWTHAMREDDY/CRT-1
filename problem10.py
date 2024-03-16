#fibanocci series
a=0
b=1
temp=0
print(a)
print(b)
for i in range(3,11):
    temp=a+b
    print(temp)
    a=b
    b=temp

#write a function to calculate sum of first and last digit of a number
def sum(a):
    b=a%10
    while a>10:
        a=a//10
    sum=b+a
    print(sum)
sum(785)
        
    

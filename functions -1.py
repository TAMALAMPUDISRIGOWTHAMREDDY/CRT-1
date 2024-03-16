#write a functon which takes two arguments a,b typecast the value of second arugment in to integer
#then multiple both the arguments and print the last digit of the result
def problem(a,b):
    b=int(b)
    c=b*a
    print(c%10)
problem(2,756.2)

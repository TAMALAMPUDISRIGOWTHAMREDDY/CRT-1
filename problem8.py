#write a program to check the type of triangle where you take input from user for 3sides and classify it accordingly in to equailateral isoceles scalen triangle
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a==b and b==c:
    print("equaletral")
elif (a==b and b!=c)or(b==c and a!=b)or(a==c and b!=a):
    print("isoceles")
else:
    print("scalene triangle")

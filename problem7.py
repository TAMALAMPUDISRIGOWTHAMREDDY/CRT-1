# checking a given year is leapyear or not
#if the yearis divisible by 4 and not div by 100 or if it is div by 400then it is called a leapyear
year=int(input("enter year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leapyear")
else:
    print("not leapyear")

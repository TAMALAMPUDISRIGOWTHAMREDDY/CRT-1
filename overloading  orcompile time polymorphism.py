#overloading or compile time polymorphism
#fuction overloading is not allowed in python it take last function in to excecution
class arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
a=arithmatic()
#a.add(10)  #error showing two argumnets missing
#a.add(10,20) #error showing one argumnets missing
a.add(10,20,30)#o/p=60

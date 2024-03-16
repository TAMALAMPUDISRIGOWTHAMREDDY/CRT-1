#create a class f-15 with functions lights ,fan and ac
#lights-when lights fun called it prints out the colour of the light is which is taken as parameter to the function
# fan -when fan fun called it display the regulator speed which is taken as parameter for the fun
# ac- ac displays the room temp and the outside temp which are taken as parameters
# write a fourth fun whose name is display which displays the diff in outside temp and room temp from of ac and also it display the fan speed
'''class f15:
    def lights(self,colour):
        self.col=colour
        print("the colour of light is",self.col)
    def fan(self,speed):
        self.sp=speed
        print("the speed is",self.sp)
    def ac(self,roomtemp,outertemp):
        self.rtemp=roomtemp
        self.otemp=outertemp
        print("the room tem is:",self.rtemp)
        print("the outer tem is:",self.otemp)
    def dif(self):
        self.diff=self.rtemp-self.otemp
        print("the diff is:",self.diff)
        print("the fan speed is:",self.sp)
a=f15()
a.lights("red")
a.fan(20)
a.ac(15,30)
a.dif()'''

'''#a is object
class f15:
    def __init__(self):                  #constructor
        a="gowtham"
        b="swetha"
        print("hello",a,b,"is calling")
    def __init__(self,e,f):                  #constructor
        print("hello",e,f,"is calling")
    def lights(self,colour):
        print("the colour of light is",colour)        #when we use the variable in  inside the function we have to declare as variable
    def fan(self,speed):
        self.sp=speed
        print("the speed is",speed)
    def ac(self,roomtemp,outertemp):
        self.rtemp=roomtemp
        self.otemp=outertemp
        print("the room tem is:",roomtemp)
        print("the outer tem is:",outertemp)
    def dif(self):
        self.diff=self.rtemp-self.otemp
        print("the diff is:",self.diff)
        print("the fan speed is:",self.sp)          #when we use the variable in out side the function we have to declare as self.variable=variable
a=f15()
a.lights("red")
a.fan(20)
a.ac(15,30)
a.dif()'''

'''class f15:
    def __init__(self,e,f):                  # parameterised constructor
        print("hello",e,f,"is calling")
    def lights(self,colour):
        print("the colour of light is",colour)        #when we use the variable in  inside the function we have to declare as variable
    def fan(self,speed):
        self.sp=speed
        print("the speed is",speed)
    def ac(self,roomtemp,outertemp):
        self.rtemp=roomtemp
        self.otemp=outertemp
        print("the room tem is:",roomtemp)
        print("the outer tem is:",outertemp)
    def dif(self):
        self.diff=self.rtemp-self.otemp
        print("the diff is:",self.diff)
        print("the fan speed is:",self.sp)          #when we use the variable in out side the function we have to declare as self.variable=variable
a=f15("gowtham","swetha")
a.lights("red")
a.fan(20)
a.ac(15,30)
a.dif()'''



class f15:
    def __init__(self,g,h):   # parameterised constructor
        self.g=g
        self.h=h
        
    def lights(self,colour):
        print("the colour of light is",colour)        #when we use the variable in  inside the function we have to declare as variable
    def fan(self,speed):
        self.sp=speed
        print("the speed is",speed)
    def ac(self,roomtemp,outertemp):
        self.rtemp=roomtemp
        self.otemp=outertemp
        print("the room tem is:",roomtemp)
        print("the outer tem is:",outertemp)
    def dif(self):
        self.diff=self.rtemp-self.otemp
        print("the diff is:",self.diff)
        print("the fan speed is:",self.sp)             #when we use the variable in out side the function we have to declare as self.variable=variable
        print("class starts at",self.g,"ends at",self.h)
a=f15(1,2)
a.lights("red")
a.fan(20)
a.ac(15,30)
a.dif()

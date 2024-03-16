'''create a class of name placements which has a function info whic displays the noof placements this year.
create another class name department with function display which will display the names of departments present in the college.
create a class pragati with a function welcome which displays the msg welcome to pragati engineering college and
this pragati class should also display the details about departments and placements'''
'''class placements:
    def info(self,no):
        self.no=no
        print("no of placements this year is:",no)
class department:
    def display(self):
        print("the name of department is it")
        print("the name of department is cse")
        print("the name of department is cse aiml")                         #multiple inheritence
        print("the name of department is eee")
        print("the name of department is ece")

class pragati(placements,department):
    def welcome(self):
        print("welcome to pragati engineering college")
c=pragati()
c.welcome()
c.info(1500)
c.display()'''


'''class placements:
    def __init__(self,no):
        self.no=no
        print("no of placements this year is:",no)
class department:
    def display(self):
        print("the name of department is it")
        print("the name of department is cse")
        print("the name of department is cse aiml")
        print("the name of department is eee")
        print("the name of department is ece")

class pragati(placements,department):
    def welcome(self):
        print("welcome to pragati engineering college")
c=pragati(1500)
c.welcome()
c.display()'''


'''class placements:
    def info(self,no):
        self.no=no
        print("no of placements this year is:",no)
class department(placements):
    def display(self):
        print("the name of department is it")
        print("the name of department is cse")
        print("the name of department is cse aiml")                         #multi inheritence
        print("the name of department is eee")
        print("the name of department is ece")

class pragati(department):
    def welcome(self):
        print("welcome to pragati engineering college")
c=pragati()
c.welcome()
c.info(1500)
c.display()'''

class placements:
    def info(self,no):
        self.no=no
        print("no of placements this year is:",no)
class department(placements):
    def display(self):
        print("the name of department is it")
        print("the name of department is cse")
        print("the name of department is cse aiml")                         #hybrid inheritence
        print("the name of department is eee")
        print("the name of department is ece")

class pragati(department,placements):
    def welcome(self):
        print("welcome to pragati engineering college")
c=pragati()
c.welcome()
c.info(1500)
c.display()

'''class placements:
    def info(self,no):
        self.no=no
        print("no of placements this year is:",no)
class department(placements):
    def display(self):
        print("the name of department is it")
        print("the name of department is cse")
        print("the name of department is cse aiml")                         #herarichal inheritence
        print("the name of department is eee")
        print("the name of department is ece")

class pragati(placements):
    def welcome(self):
        print("welcome to pragati engineering college")
c=pragati()
c.welcome()
c.info(1500)
d=department()
d.display()'''

        
        
        

class faculty:
    def __init__(self,fname,dep,no):
        self.fname=fname
        self.dep=dep
        self.no=no
    def print(self):
        print("fname is",self.fname,"dep is",self.dep,"no is",self.no)
obj=faculty("gowtham","It",1)
obj.print()
class student(faculty):
    def abc(self):
        pass
obj1=student("swetha","cse",1)
obj1.print()

                 

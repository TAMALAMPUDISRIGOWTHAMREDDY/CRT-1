 #write a login function which accepts the user only when user name and password are same and display a msg login successful
#otherwise it keeps asking the user to enter the creditanals until they are correct
def fun():
    while 1:   #in place of 1 we can place True and any other to  run infinite loop
        login=input()
        password=input()
        if login==password:
            print("login successful")
            break  
fun()

#Global variable and local variable
a = 10

def something():
    global a
    a = 15
    print("In function ",a)
    
something()

print("Outside function ",a)
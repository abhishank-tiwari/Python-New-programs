def calc(z,y,n):
    
    if n == 1:
        x = lambda a,b : a + b
        c = x(z,y)
        return c
    elif n ==2:
        x = lambda a,b : a - b
        c = x(z,y)
        return c
    elif n == 3:
        x = lambda a,b : a*b
        c = x(z,y)
        return c
    else:
        x = lambda a,b : a/b
        c = x(z,y)
        return c

z = int(input("First number"))
y = int(input("Enter second number"))
print(" Type 1 for addition","\n","Type 2 for substraction","\n","Type 3 for Multiplication","\n","Type 4 for Division")
n = int(input(""))
print("Result is : ",calc(z,y,n))

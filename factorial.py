def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
        
    return f

x = int(input("Enter the number whose factorial to be found : "))
result = fact(x)

print("Factorial of ",x," is :",result)
def sum(a,*b):
    c= a
    for i in b:
        c = c + i
        
    return c

print(sum(5,4,3,8,9))
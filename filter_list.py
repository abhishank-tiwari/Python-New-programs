def seg(x):
    if x%2 ==0:
        return x
    else:
        pass
    
lst = [5, 6, 2, 7, 9 , 11] 

y = list(filter(seg,lst))
print(y)
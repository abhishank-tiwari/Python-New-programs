def count(lst):
    even = 0
    odd = 0
    
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
            
    return even, odd

lst = [ 5,6,7,8,3,1,9,11,23,21,12,14]

e,o = count(lst)

print("Num of even in list is ",e," and odd in list is ",o)
            
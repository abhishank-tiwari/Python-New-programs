lst = [5, 3 ,1, 4, 2]
i = 0
result = 0
while i < len(lst):
    num = lst[i]
    result = num + result
    i += 1
    
print("Sum of list elements ",lst," is ",result)
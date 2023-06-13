#print even elements in a list
lst = [55,49,36,63,18]
x = list(filter(lambda x : x%2 == 0 , lst))
print(x)
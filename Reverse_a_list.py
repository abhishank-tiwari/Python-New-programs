#Reverse a list
a = [ 5,6,7,9,2]

x = len(a)
b = []
for i in range(x):
    c = x-i-1
    h = a[c]
    b.append(h)

print(b)
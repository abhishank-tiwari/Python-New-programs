#Count occurrence of an element in a list

lst = [ 5,6,7,8,6,7,9,6,4,6]

c = 0
print("List is ",lst)
x = int(input("Enter element whose occurrence to be find above list"))

for ele in lst:
    if ele == x:
        c = c + 1
  

print(x," occurs ",c," times")
    
#Appending a list

a = []
n = int(input("Enter number of elements to be added in list "))
for i in range(n):
    x = input("Enter item to be added in the list")
    a.append(x)
    
print("Appended list is as folows ")
print(a)
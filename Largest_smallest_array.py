#Write a program to find largest and smallest
arr = []
n = int(input("Enter size of an array : "))
for x in range(n):
    y = int(input("Enter element of an array : "))
    arr.append(y)
    
largest = arr[0]
smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]
        
print(f"largest array is {largest}")
print(f"Smallest array is {smallest}")
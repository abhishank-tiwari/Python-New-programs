#Sum of n natural numbers
n = int(input("Enter number upto which you want to do sum of Natural numbers"))
i = 1
sum = 0

for i in range(n):
    sum = sum + i
    i = i + 1
    
print("Sum of n  natural number is : ", sum)
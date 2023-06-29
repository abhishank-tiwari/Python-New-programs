#Find to square root of a number
import math
num = int(input("Enter a number whose sqare root to be found : "))

if num < 0:
    print("Negative numbers don'nt have square roots")
else:
    print("Square root of ",num," is ",math.sqrt(num))
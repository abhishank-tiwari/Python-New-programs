#Program to remove blank spaces in a string
string = input("Enter a string : ")
result =''

for i in string:
        if i!= ' ':
            result = result + i
        
print("Corrected string is : ",result)
    
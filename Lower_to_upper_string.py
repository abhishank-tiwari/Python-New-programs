#Converting lower characters of a string to Upper case
string = input("Enter a string : ")
result = ''
for i in string:
    if i.islower():
        i = i.upper()
    result = result + i
    
print("String after converting lower case to upper case : ",result)
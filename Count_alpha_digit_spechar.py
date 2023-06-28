#Python program to enter a string and count alphabets , digits and special characters
string = input("Enter a string : ")
alphabets = 0
digits = 0
SpecialChars = 0
for i in string:
#Counts number of alphabets in a string
    if i.isalpha():
        alphabets += 1
#Count number of digits in a string
    elif i.isdigit():
        digits += 1
#Count number of special character in a string
    else:
        SpecialChars += 1
        
print("Number of alpahbets : ",alphabets," , Number of digits :  ",digits," , Number of special character : ",SpecialChars)

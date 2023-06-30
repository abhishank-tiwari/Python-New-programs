#Python program to sort string in descending order
string = input("Enter the string : ")
strlist = list(string)
sortedstring = ''.join(sorted(strlist,reverse = True))
print("String sorted in ascending order : ",sortedstring)
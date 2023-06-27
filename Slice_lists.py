#Python program to slice lists
#Get all the elements
print("Get all the elements ")
my_list = [1,2,3,4,5,6]
print(my_list[:])
#Print all elements after position 2
print("All elements after position 2 ")
print(my_list[2:])
#Print all elements before position 2
print("Print all elements before position 2")
print(my_list[:2])
#Get all elements from one position to another position
print("Get all elements from 3rd position to 4th position ")
print(my_list[3:5])
#Get the Items at Specified Intervals
print("Get the Items at Specified Intervals ")
print(my_list[::2])
#If you want the indexing to start from the last item
print("If you want the indexing to start from the last item")
print(my_list[::-2])
#Get the Items at Specified Intervals from one position to another position
print("Get the Items at Specified Intervals from one position to another position")
print(my_list[1:4:2])
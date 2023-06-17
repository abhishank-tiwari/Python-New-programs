#Input single dimensional array
def take_array_input():
    input_string = input("Enter elements of an array seperated by commas : ")
    input_list = input_string.split(",")
    array = [int(element) for element in input_list]
    return array

my_array = take_array_input()
print("Array : ",my_array)
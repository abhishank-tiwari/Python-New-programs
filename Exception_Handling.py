#Exception Handling
a = input("Enter an integer ")
b = input("Enter an integer ")
try:
	print("Resource open")
	print(int(a)/int(b))


except ZeroDivisionError as e:
	print("Hey,You can not divide a number by Zero",e)
except ValueError as e :
	print("Invalid Input")
except Exception as e:
	print("Something went wrong")
finally:
	print("Resource closed")
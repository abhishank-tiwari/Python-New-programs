#Program to display calender of a given month and year
#Importing calendar module
import calendar
yy = int(input("Enter the year whose calendar to be found "))
mm = int(input("Enter the month whose calendar to be found "))
print(calendar.month(yy,mm))
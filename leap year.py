input_year = int(input("Enter the Year to be checked: "))
if (input_year%400 == 0):
          print("%d is a Leap Year" %input_year)
elif (input_year%100 == 0):
          print("%d is Not the Leap Year" %input_year)
elif (input_year%4 == 0):
          print("%d is a Leap Year" %input_year)
else:
          print("%d is Not the Leap Year" %input_year)

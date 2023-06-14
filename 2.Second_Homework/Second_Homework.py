#First xersize======================================================================
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choise = input("Choose an option:\n[ + ].Adding\n[ * ].Multiplication\n")
if choise == "+":
    print("The summ is: ", + (a+b))
elif choise == "*":
    print("The product is: ", + (a*b))
else:
    print("Wrong choise.")

#Second exersize=====================================================================
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
numbers = [a,b,c]
largest = max(numbers)
smalest = min(numbers)
average = (a+b+c)/3
choise = input("Choose an option:\n[ max ].Maximum\n[ min ].Minimum\n[ avg ].Average\n")
if choise == "max":
    print("The largest number is: ", + largest)
elif choise == "min":
    print("The smalest number is: ", + smalest)
elif choise == "avg":
    print("The average is: ", + average)
else:
    print("Wrong choise.")

#Third exersize=============================================================
meters = int(input("Enter length in meters: "))
miles = meters / 1609
inches = meters * 39.37
yards = meters * 1.093
choise = input("Choose a parameter to convert:\n[ miles ]\n[ inches ]\n[ yards ]\n")
if choise == "miles":
    print("The distance in miles is: ", + miles)
elif choise == "inches":
    print("The distance in inches is: ", + inches)
elif choise == "yards":
    print("The distance in yards is: ", + yards)
else:
    print("Wrong choise.")

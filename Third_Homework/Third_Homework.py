#==========================#1================================
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
#==========================#2================================
number = int(input("Enter number: "))
if number % 7 == 0:
    print("Number is multiple of 7.")
else:
     print("Number is  notmultiple of 7.")
#==========================#3================================
n_list=[]
n_list.append(int(input("Enter number: ")))
n_list.append(int(input("Enter number: ")))
print("Maximum is: ",+ max(n_list))
#==========================#4================================
n_list=[]
n_list.append(int(input("Enter number: ")))
n_list.append(int(input("Enter number: ")))
print("Minimum is: ",+ min(n_list))
#==========================#5================================
n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
choise = int(input("Make your choise:\n1. Summ\n2.Difference.\n3.AVG. "))
if choise == 1:
    print("The summ is: ", (n1+n2))
elif choise == 2:
    print("The difference is: ", (n1-n2))
elif choise == 3:
    print("The AVG is: ", (n1+n2)/2)
else:
    print("Wrong choise.")
#==========================#6================================
print("Enter the number of the day.")
number = int(input())
if number==1:
    print("Sunday.")
elif number==2:
    print("Monday.")
elif number==3:
    print("Tusday.")
elif number==4:
    print("Wednesday.")
elif number==5:
    print("Thurthday.")
elif number==6:
    print("Friday.")
elif number==7:
    print("Saturday.")
else:
    print("Wrong choise.")
#==========================#7================================
print("Enter the number of the month.")
number = int(input())
if number==1:
    print("January.")
elif number==2:
    print("February.")
elif number==3:
    print("March.")
elif number==4:
    print("April.")
elif number==5:
    print("May.")
elif number==6:
    print("Jun.")
elif number==7:
    print("July.")
elif number==8:
    print("August.")
elif number==9:
    print("September.")
elif number==10:
    print("October.")
elif number==11:
    print("Nowember.")
elif number==12:
    print("Decomber.")

else:
    print("Wrong choise.")
#==========================#8================================
number = int(input("Enter number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is equale to zero.")
#==========================#9================================
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a == b:
    print("a = b .")
elif a < b:
    print("a < b .[",+ a,";",+ b,"]")
elif a > b:
    print("a > b .[",+ b,";",+ a,"]")
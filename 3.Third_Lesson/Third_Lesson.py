'''
prog_lang = ["C#", "C++", "Python","JavaScript","GO"]
print(type(prog_lang))
print(type(prog_lang[0]))
print(prog_lang[-1])
print(len(prog_lang))
prog_lang.append("TypeScript")
print("==============append==============")
print(prog_lang)
print("==============remove==============")
prog_lang.remove("TypeScript")
print(prog_lang)
print("==============insert==============")
prog_lang.insert(2,"Kotlin")
print(prog_lang)
print("==============pop==============")
prog_lang.pop(1,)
print(prog_lang)
print("==============reverse==============")
prog_lang.reverse()
print(prog_lang)
print("==============sort==============")
prog_lang.sort(reverse=True)
print(prog_lang)
'''
#==================================================================================
'''
mix_list = [1,2,-3,"Apple",[22,"Peanapple"],False]
print(mix_list)
print(type(mix_list[4][1]))
print("==============reverse==============")
mix_list[4].reverse()
print(mix_list)
'''
'''my_list =[]
my_list.append(int(input("Enter number ")))
my_list.append(int(input("Enter number ")))
my_list.append(int(input("Enter number ")))
my_list.append(int(input("Enter number ")))
my_list.append(int(input("Enter number ")))
summ = (my_list[0]+my_list[1]+my_list[2]+my_list[3]+my_list[4])
averge = ((my_list[0]+my_list[1]+my_list[2]+my_list[3]+my_list[4])/5)
print("Summ = ",+summ,"\n")
print("Averge = ",+averge,"\n")'''
'''my_list = []
size = 5
for i in range(size):
    my_list.append(int(input("Enter number ")))
summ = (my_list[0]+my_list[1]+my_list[2]+my_list[3]+my_list[4])
averge = ((my_list[0]+my_list[1]+my_list[2]+my_list[3]+my_list[4])/5)
print("Summ = ",+summ)
print("Averge = ",+averge)'''
'''Користувач вводить із клавіатури час у секундах, що минув від початку дня. 
Залежно від вибору користувача потрібно порахувати скільки годин, 
хвилин і секунд залишилося до опівночі.'''
'''user_time = int(input("Enter numder of seconds: "))
time = 86400 - user_time
hours = int(time/3600)
minutes = int((time - (hours*3600))/60)
seconds = int(time - (hours*3600)-(minutes*60))
print(hours)
print(minutes)
print(seconds)'''
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
    print("The AVG is: ", (n1-n2)/2)
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
elif number==1:
    print("Friday.")
elif number==1:
    print("Saturday.")
else:
    print("Wrong choise.")

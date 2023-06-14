#===================LOOPS==============
#people = ["John","Adam","Sarah","Paul","Eva"]
'''for person in people:
    print(person)'''
'''for person in people:
    if person == "Sarah":
        print(person)
        print(f"Index of wanted element: {people.index(person)}")'''
        
'''for i in range(len(people)):
    print(people[i])'''
'''count = 1
#number = int(input("Enter number: "))
number =1

while count < 10:
    print(number," * ",+ count," = ", +(number*count))
    count += 1 
number += 1
'''
'''exit = False
while exit != True:
    choise = int(input(f"Buy 36.57\tSale 37.45\n1. Buy\n2. Sell\n0. Exit\n"))
    if choise ==1:
        money = int(input(f"How many dolars do you want to buy? "))
        print(f"You must pay {int (money * 37.45)} uah")
    elif choise == 2:
        money = int(input(f"How many uah do you have? "))
        print(f"You earn {int (money / 36.57)} usd")
    elif choise ==0:
        exit=True'''
'''a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))
ex = False
while ex == False:
    c = int(input("Enter your number: "))
    if c >=a and c <=b:
        for var in range(a,b+1):
            ex = True
            if var == c:
                print(f"!{var}!", end=" ")
            else:
                print(var, end=" ")  
    else:
        print("Out of range.")'''
'''import random
x = random.randint(1,500)
ex = False
tryes = 10
while ex == False and tryes > 0:
    u = int(input(f"Gues the number(you have {tryes} tryes): "))
    if u == x:
        print(f"You win! The guessed number is {u} ")
        ex = True
    elif u < x and tryes > 1:
        print("Ops... Sims like you have try some larger number")
        tryes -=1
    elif u > x and tryes > 1:
        print("Ops... Sims like you have try some smaler number")
        tryes -=1
    else:
        print("You lose :(")
        ex =True'''
'''my_list = []
ex = False
counter = 0
while ex ==False:
    ch=int(input("1. Add element to list.\n0. Exit\n"))
    if ch == 0:
        ex = True
    elif ch == 1:
        my_list.append(int(input("Enter new element: ")))
    else:
        print("Wrong choise.")
chsec=int(input("Enter wanted number.\n"))
for var in range(len(my_list)):
    if chsec == my_list[var]:
        counter +=1
print(f"Your number repeated {counter} times.")'''

    
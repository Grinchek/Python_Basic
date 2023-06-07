import random

number = int(input("Enter day number: "))
# print(f"{number}")
# number = random.randint(1, 7)
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuseday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("There are no days with this number.")

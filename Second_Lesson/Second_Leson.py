# number = int(input("Enter day number: "))
# # print(f"{number}")
# # number = random.randint(1, 7)
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuseday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("There are no days with this number.")
# a = int(input("Enter a "))
# b = int(input("Enter b "))
# print("Summ", a+b, "\nDiference", a-b, "\nProduction", a*b, "\nDivision", a/b)
# if a > b:
#     print("Max ", a, ", Min", b)
# elif a < b:22
#     print("Max", b, ", Min", a)
# else:
#     print("a = b")
# print("Average number ", (a+b)/2)
a = int(input("Enter hour: "))
if a >= 0 and a <= 6:
    print("Good night")
elif a > 6 and a <= 13:
    print("Good morning")
elif a > 13 and a <= 17:
    print("Good day")
elif a > 17 and a <= 23:
    print("Good evening")

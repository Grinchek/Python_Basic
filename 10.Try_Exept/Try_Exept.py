from math import sqrt



# try:
#     num = int(input("Enter number, to find out it squere root: "))
#     print(f"The squear root of {num} is: {sqrt(num)}")
# except ValueError:
#     print("Wrong input ")


# def squere(num):
#     return sqrt(num)
# try:
#     num = int(input("Enter number to find out it squere root: "))
#     squere(num)
#     print(squere(num))
# except ValueError:
#     print("Error!")
my_dictionary = {}

ex=False
while ex !=True:
    us_choice= int(input("1.Add item \n0.Exit "))
    if us_choice==1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dictionary[key]=value
    elif us_choice==0:
        ex=True
while ex !=False:
    action = int(input("1.Show all\n2.Search by value\n3.Change value\n4.Search by key\n5.Clear value\n0.Exit"))
    if action== 1:
        print(my_dictionary)
    elif action==2:
        us_value = input("Enter value: ")
        for key in my_dictionary:
            if us_value == value:
                print(key)
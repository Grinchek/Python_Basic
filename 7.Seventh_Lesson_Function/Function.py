#========================1====================
# def sum(*numbers):
#     res = 0
#     for item in numbers:
#         res +=item
#     print(f"Sum = {res}")
# sum(2,3,4,5,6,7,8,9)
#==========================2==================
# def max(*numbers):
#     max=0
#     for i in range(len(numbers)-1):
#         if numbers[i]>numbers[i-1]:
#             max = numbers[i]
#     print(f"Maximum = {max}")
# max(1,3,6,18,7)
#======================3======================
# def types(*numbers):
#     equal=0
#     odd = 0
#     positive = 0
#     negative =0
#     for i in range(len(numbers)):
#         if numbers[i] %2 == 0:
#             equal+=1
#         elif numbers[i] %2 != 0:
#             odd+=1
#         if numbers[i] > 0:
#             positive+=1
#         elif numbers[i] < 0:
#             negative+=1
#     print(f"Equal: {equal}\nOdd: {odd}\nPositive: {positive}\nNegative: {negative}")
# types(-2,4,56,-45,11,88,-234)
#===================4====================
# def reverse(list):
#     list.reverse()
#     print(list)
# list=[1,2,3,4,5,6,7,8,9]
# reverse(list)
#======================5==============
# my_list=[1,2,3,4,5,6,7,8,9]
# def find(list):
#     uin = int(input("Enter searched number:"))
#     for i in range(len(my_list)):
#         if uin in my_list:
#             print(f"Success: {uin}")
#             break
#         else:
#             print("Error.")
#             break
# find(my_list)
# varible a for define a desteny to the dacha
# varible b for define, how many liters of petrol we net to drive 100 km 
# variable c for define price of petrol
# cost = lambda a,b,c: (((a/100)*b*c)*2)

# a= int(input("Enter a destiny:"))
# b= int(input("Enter a consumption:"))
# c= int(input("Enter a prise for the litr of petrol:"))
# print(f"You have to pay {cost(a,b,c)} uah for your trip")
#======================7===================
# distance = int(input("Enter distance(in meter):"))
# time = int(input("Enter time(in seconds):"))
# speed = lambda distance, time: (distance/1000)/(time/3600)
# print(f"Sportsmen's speed:{speed(distance,time)} km\hour")
#======================8================================
# Написати калькулятор, робота якого буде основана на функціях.
# Введення цифр та вибір математичної операції виконати в діалоговому стилі 
# (запитати у користувача, вивести меню). У програмі передбачити уникнення помилок
# (ділення на нуль і т.д.). Фантазія та «дизайн» меню – ціниться та вітається!!!
# Примітка! Кожна арифметична операція описується окремою функцією.
# Побудова самого меню також винесена в окрему функцію.
# def calc(a,b,sign):
#     res = 0
#     if sign == '+':
#         res = (a + b)
#         print(f"{res}",end="")
#     elif sign=='-':
#         res = (a - b)
#         print(f"{res}",end="")
#     elif sign=='*':
#         res = (a * b)
#         print(f"{res}",end="")
#     elif sign == '/'and b !=0:
#         res = (a / b)
#         print(f"{res}",end="")
#     else:
#         ex = True
# ex = False
# while ex == False:
#     a = int(input("> "))
#     sign = input(" ")
#     b = int(input("> "))
#     calc(a,b,sign)
#===========================9=================================
# Написати наступні функції, які в якості параметра приймають одновимірний масив 
# і його розмірністю. 
# Перевірити роботу функції для одновимірних масивів довжини 10 та довжини 7.
# функцію Fill(), яка заповнює одновимірний масив випадковими значеннями в діапазоні [-12..20]
# шаблонну функцію Print(), 
# яка виводить елементи масиву на екран. Примітка!
# Протестувати дану функцію на масивах типу int, double, char
# функцію, яка повертає кількість відємних елементів масиву
# перевантажені функції:
# - для знаходження середнього арифметичного елементів масиву
# - для знаходження максимального елемента масиву в проміжку
# (між двома вказаними індексами)
import random
my_list = []
my_list.clear
size = int(input("Size = "))
def fill(list,size):
    for i in range(size):
        my_list.append(random.randint(-12,20))
def average(lst):
    return sum(my_list) / len(my_list)
fill(my_list,size)
print(my_list)
print(f"Averange: {average(my_list)}")
def max_in_range(list):
    start= int(input("Start: "))
    end= int(input("End: "))
    for i in range( my_list[start:end]):
        if my_list[i]>my_list[i+1]:
            print(f"Max: {my_list[i]}")
max_in_range(my_list)


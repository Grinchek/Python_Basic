'''person = {
    "FirstName" : "Bill",
    "LastName" : "Gates",
    "Age" : 24
}'''
#print(f"type: {type(person)}\nValue: {person['FirstName']}\nSurname: {person['LastName']}\nAge: {person['Age']}")
#print(person.get('LastName'))
#print(person.keys())
#print(person.items())
#person2 = person.copy()
#person2['Age'] = 30
#print(person.get('Age'))


#people_list = [person,person2]
#print(people_list)
#print(people_list[1].get('Age'))
#print(people_list[0]['Age'])
#for item in people_list:
    #print(item['Age'])  
'''user_input = input("Enter yor text: ")
user_input = user_input.split()
my_dict_list = {}
for word in user_input:
    if word in my_dict_list:
        my_dict_list[word]+=1
    else:
        my_dict_list[word]=1

print(my_dict_list)'''
'''ex = False
sum = 0
while ex !=True:
    num = int(input("Enter number: "))
    if num != 0:
         sum +=num
    else:
         ex = True
      
        
print(sum)
'''
'''num = float(input("Enter number: "))
if num == 1 or num % num == 0:
    print(f"Yor number {num} is simle number.")
else:
    print(f"Yor number {num} is not simle number.")'''
import random
my_list = []
for i in range(5):
    my_list.append(random.randint(1,10))
print(my_list)
choise = int(input("Make you choise, to sort array:1.Upper\n2.Lower."))

if choise == 1:
    for i in range(4):
        for j in range(5-i-1):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
elif choise ==2:
    for i in range(4):
        for j in range(5-i-1):
            if my_list[j]<my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
else:
    print("Wrong choise.")        
print(my_list)

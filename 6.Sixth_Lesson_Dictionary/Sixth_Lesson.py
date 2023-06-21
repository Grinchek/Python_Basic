person = {
    "FirstName" : "Bill",
    "LastName" : "Gates",
    "Age" : 24
}
#print(f"type: {type(person)}\nValue: {person['FirstName']}\nSurname: {person['LastName']}\nAge: {person['Age']}")
#print(person.get('LastName'))
#print(person.keys())
#print(person.items())
person2 = person.copy()
person2['Age'] = 30
#print(person.get('Age'))


people_list = [person,person2]
#print(people_list)
#print(people_list[1].get('Age'))
#print(people_list[0]['Age'])
#for item in people_list:
    #print(item['Age'])
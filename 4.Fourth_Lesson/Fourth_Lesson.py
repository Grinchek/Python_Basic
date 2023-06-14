#===================LOOPS==============
people = ["John","Adam","Sarah","Paul","Eva"]
'''for person in people:
    print(person)'''
for person in people:
    if person == "Sarah":
        print(person)
        print(f"Index of wanted element: {people.index(person)}")
        
'''for i in range(len(people)):
    print(people[i])'''
'''count = 0
while count < 10:
    print(f"Count: {count}")
    count += 1 '''
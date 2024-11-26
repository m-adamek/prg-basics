# Create a dictionary as in the example below. Do you know what type of value was used in each of the six key-value pairs?

# Then, create a program that:

#1 Displays name
#2 Displays hobby
#3 Displays the entire contents of the dictionary
#4 Changes surname to 'Nowak'
#5 Changes person's marriage status
#6 Adds gender: 'male'
#7 Adds a new hobby: 'bicycle'
#8 Adds work phone to existing phones: '313131444'
#9 Displays the entire contents of the dictionary (iterate over dictionary items)


person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

#1
print(f"Name: {person['name']}")

#2
print(f"Hobby: {person['hobby']}")

#3
print(f"Dictionary: {person}")

#4
person['surname'] = "Nowak"
print(person['surname'])

#5
person['married'] = False
print(person['married'])

#6
person['gender'] = 'male'
print(person['gender'])

#7
person["hobby"].append("bicycle")

#8
person["phone"]["work"] = "313131444"

#9
for key, value in person.items():
    print(f"{key} : {value}")
# Write a program that checks that both people are adults. Read people's data from the keyboard.

###
# Checking if both people are adults
#
person1_name = input("Enter the first person's name: ")
person1_age = int(input("Enter the first person's age: "))
person2_name = input("Enter the second person's name: ")
person2_age = int(input("Enter first person's age: "))

if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')
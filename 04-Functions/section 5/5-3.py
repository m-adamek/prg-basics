###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard as key

# Reads employee's data from keyboard
first_name = key.input_string("Enter employee's name: ")
last_name = key.input_string("Enter employee's last name: ")
age = key.input_integer("Enter employee's age: ")
salary = key.input_real("Enter employee's salary: ")
is_salary_hidden = key.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name + " " + last_name)
print("Age: ", age)
if is_salary_hidden == False:
    print('Salary: ', salary)
elif is_salary_hidden == True:
    print("The salary is hidden.")
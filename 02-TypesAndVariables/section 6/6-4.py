###
# A program for printing detailed information.
# Print the employee's name, surname, initials and date of birth on separate lines. Complete the following program code.

employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[22:]}')
print(f'Initials: {employee[4] + employee[9]}')
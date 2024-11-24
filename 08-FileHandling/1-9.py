# The file it_company.csv contains a list of employees.
# Write a program that displays only employees with the position "Software Engineer".
# Number the items on the printed list.

# Hint: You can check if a string is contained within another string using the 'in' operator.

###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, "r") as file:
   file_lines = file.splitlines()
   number = 1
  
   for line in file_lines:
      if job_title in line:
        number+=1
        numbered = str(number) + "."
        print(numbered,line)
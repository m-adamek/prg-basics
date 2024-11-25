# Write a program that saves data of employees employed in the position of
# 'Software Engineer' to the file 'software_engineer.txt'. 
# Data is available in the file 'it_company.csv'.

# Hint: Read employee data line by line.
# For each line, check if it contains the name of the indicated position.
# If so, write this line to the output file.

###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, "r") as employees_txt:
   employees = employees_txt.read()
   employees_lines = employees.splitlines()
   
   with open(position_file, "w") as position:
      for line in employees_lines:
         if job_title in line:
            position.write(f"{line}\n")



### ver 2
# Saves to a file a list of employees working at a specified position.

# # File names
# employees_file = 'it_company.csv'
# position_file = 'software_engineer.txt'

# # Position 
# job_title = 'Software Engineer'

# # Write selected employees to a file
# with open(employees_file, "r") as employees_txt:
#     employees_lines = employees_txt.readlines()  # Read lines from the input file

#     with open(position_file, "w") as position:
#         for line in employees_lines:
#             if job_title in line:  # Check if the job title is in the current line
#                 position.write(line)  # Write the matching line to the output file

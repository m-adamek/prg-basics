# The file pets.txt contains humorous text about animals.
#  Write a program that prints the text and counts the number of words in the text.

# To calculate the number of words in a line, use the split() method,
# which splits a string into a list where each word is a list item.
# Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.
# https://www.w3schools.com/python/ref_string_split.asp

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

total = 0
file_content = read_from_file("pets.txt")
file_lines = file_content.splitlines()
print(file_lines)

for line in file_lines:
   words = line.split()
   total += len(words)

print(total, "words")
print(file_content)
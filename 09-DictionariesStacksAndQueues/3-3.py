# Define a function that returns true if the brackets (), {}, [] are used correctly in the given expression.
# Otherwise, the function returns false.
# Then write a program that checks the correctness of the expressions given below.

# Use a stack. Read the next characters of the expression.
# Skip all but the brackets. If it is an opening bracket, put it on the stack.
# If it is a closing bracket, get the item from the stack and compare whether it is a matching opening bracket.

import queue

# expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
# expression2 = "[(2+3]/4)"                 # brackets not correct
# expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack = 

   return #True if brackets in expression are ok or False otherwise




if brackets_ok(expression1):
   print(f"The brackets in {expression1} are correct.")
else:
   print(f"The brackets in {expression1} are not correct.")

if brackets_ok(expression2):
   print(f"The brackets in {expression2} are correct.")
else:
   print(f"The brackets in {expression2} are not correct.")

if brackets_ok(expression3):
   print(f"The brackets in {expression3} are correct.")
else:
   print(f"The brackets in {expression3} are not correct.")
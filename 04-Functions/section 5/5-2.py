# The converters.py file defines two functions for converting length units (cm-->m and m-->cm). 
# The test_converters.py file uses these functions to convert values.

# Define the following functions in the converters.py file that allow you to:

# convert centimeters to inches
# convert feet and inches to centimeters
# Then complete the main program to test the added functions.

import converters as con

print(f'2m = {con.m_to_cm(2)}cm')
print(f'532cm = {con.cm_to_m(532)}m')
print(f"60cm = {con.cm_to_inch(60)}inches")
print(f"7 feet and 6 inches is {con.feet_inches_to_cm(7,6)} cm")

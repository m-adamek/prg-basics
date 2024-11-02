###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string = str(input(message))
    return string

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    boolean_con = str(input(message))
    if boolean_con.lower() == "y":
        return True
    elif boolean_con.lower() == "n":
        return False


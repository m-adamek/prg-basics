def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n * 0.3937

def feet_inches_to_cm(n,m):
    feet = n * 30.48
    inches = m * 2.54
    cm = feet + inches
    return cm

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"60cm = {cm_to_inch(60)}inches")
    print(f"7 feet and 6 inches is {feet_inches_to_cm(7,6)} cm")

# Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23)
# and the number of minutes (0..59), returns a string specifying the time in the given format
# ('24' for 24-hour time and '12' for 12-hour time).

# Then write a program that tests whether the function works correctly.

# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 02, '12') returns '7:02pm'
# Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings'.

def time_string(hours, minutes, time_format):
    result = ''
    if time_format == '12':
        result = ''
        
        if hours > 12: 
            pm_hours = hours - 12
            str_hours = str(pm_hours)
        elif hours <= 12 and hours != 0:
            str_hours = str(hours)
        elif hours == 0:
            hours = hours + 12
            str_hours = str(hours)
        
        if minutes < 10:
            str_minutes = str(minutes)
            str_minutes = "0" + str_minutes
        elif minutes >=10:
            str_minutes = str(minutes)

        if hours >= 12:
            result = str_hours + ":" + str_minutes + "pm"
        elif hours < 12 or hours == 0:
            result = str_hours + ":" + str_minutes + "am"
        
            
    elif time_format == '24':
        str_hours = str(hours)
        if minutes < 10:
            str_minutes = str(minutes)
            str_minutes = "0" + str_minutes
        if minutes >=10:
            str_minutes = str(minutes)
        result = str_hours + ":" + str_minutes
    
    return result

print(time_string(15, 38, '24')) 
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12')) 

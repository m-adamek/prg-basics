# Define a function that calculates the final grade for a test based on the number of points obtained,
# according to the rules:

# Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent

def pts_to_grade(points):
    if points >= 18:
        return ("Excellent")
    elif points >=14:
        return ("Good")
    elif points >= 10:
        return ("Satisfactory")
    elif points <10:
        return ("Fail")

test_result = int(input("Enter your points: "))
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
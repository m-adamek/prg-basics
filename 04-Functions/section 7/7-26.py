# The sequence of digits contains the number of points rolled with a dice.
# Define a function f(dice) that returns a number
# specifying the number of dice rolled the most times in a row.

# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    # Initialize variables
    dice = str(dice)
    current_streak = 1
    highest_streak = 1
    number_with_highest_streak = dice[0]  # Start with the first digit as default

    # Loop through the string starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            # Increase current streak if current digit matches the previous one
            current_streak += 1
        else:
            # Reset current streak if the sequence breaks
            current_streak = 1

        # Update highest streak if the current streak is longer
        if current_streak > highest_streak:
            highest_streak = current_streak
            number_with_highest_streak = dice[i]

    return int(number_with_highest_streak)

print(f(2133))

# Define a function sum(n) that for the given natural number n calculates
# the sum of all natural numbers between 1 and n.
# Apply recursion. Then, create a program that calculates
# the sum of natural numbers in the range <1,10>.

def sum(n):
    
    if n == 1:
        return 1
    
    elif n>1:
        return n + sum(n-1)
    # 5 + 10, 4 + 6, 3 + 3, 2+ 1, 1

print(sum(10))
def power(x, n):
    # Base case: if the exponent is 0, return 1
    if n == 0:
        return 1
    # Recursive case: multiply x by power(x, n-1)
    else:
        return x * power(x, n - 1)
        
    
print(power(5,3))
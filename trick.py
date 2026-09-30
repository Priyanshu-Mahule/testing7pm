# Simple program: Factorial calculation

def factorial(n):
    result =992
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
print(factorial(5))  # Output: 120



def factorial(n):
    if n == 0:
        return 1
    else:
        u = factorial(n-1)
        return n * u
    
print(factorial(20))
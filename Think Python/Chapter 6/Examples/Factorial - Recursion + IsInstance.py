# My version of the example in the book, the title of the section is "Checking Types", i prefere to use more a general and consice version using a nested conditional to include both  isinstance() function and n >= 0 with an and operator. I liked it, so I personally encourage you to try things out. It's outstanding the self-realization. Anyways, thank you :)
def factorial(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 1
        else:
            u = factorial(n-1)
            return n * u
    else:
        return "Just positive integers please ;~)"
    
print(factorial(1.5))
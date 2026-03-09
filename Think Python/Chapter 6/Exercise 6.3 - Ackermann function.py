""" The Ackermann function, A m, n , is defined as:
A m, n =
n + 1  ----- if m = 0
A(m - 1, 1) ----- if m > 0 and n = 0
A (m - 1, A (m, n - 1)) ----- if m > 0 and n > 0 .
Write a function named ackermann that evaluates the Ackermann function. What
happens if you call ackermann(5, 5)? """

def A(m,n):
    if  m == 0:
        return n+1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
    else:
        return False

print(A(3,6))
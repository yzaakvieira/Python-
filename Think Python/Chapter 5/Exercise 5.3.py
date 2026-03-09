# What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the result.
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 2)w
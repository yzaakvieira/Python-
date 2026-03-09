# Write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height, made up of copies of the string. Here’s an example of a rectangle with width 5 and height 4, using the string 'H'

def rectangle (a,b, c):
    # b = column 
    # c = line
    for _ in range(1, c + 1):
        e = a*b 
        print( e)
        
rectangle("S", 5, 4)
# Write a boolean function, is_between(x, y, z), that returns True if x < y < z or if z < y < x, and False otherwise.

def is_between(x,y,z):
    if x < y < z or z < y < x:
        return True
    else:
        return False

print(is_between(10,20,39))
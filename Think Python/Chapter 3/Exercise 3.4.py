# The song “99 Bottles of Beer” starts with this verse:
#  99 bottles of beer on the wall, 
#  99 bottles of beer. 
#  Take one down, pass it around,
#  98 bottles of beer on the wall.
#  Then the second verse is the same, except that it starts with 98 bottles and ends with 97. The song continues—for a very long time—until there are 0 bottles of beer. Write a function called bottle_verse that takes a number as a parameter and displays the verse that starts with the given number of bottles.
# Hint: consider starting with a function that can print the first, second, or last line of 
# the verse, and then use it to write bottle_verse.

def bottle_verse(a):
   print(f"""
    {a} bottles of beer on the wall,
    {a} bottles of beer.
    Take one down, pass it around,
    {a-1} bottles of beer on the wall.   """)
   
bottle_verse(110)
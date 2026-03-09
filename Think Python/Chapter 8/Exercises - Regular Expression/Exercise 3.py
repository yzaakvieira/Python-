# Fiding all numbers in a text file
import re 
reader = open("Python 3.txt", encoding = "utf-8")

def finding_numbers():

    for line in reader:
        numbers = re.findall(r"\d+", line)
        # findall - Returns a list of characters. 
        # r - Raw string; It returns a string without superpowers of the interpreter, and use it like literal string, without the superpower, like \n.
        # \d - It's a method to return the digit | + - It returns the adjacent sequence of elements and put all together.
        
        if numbers: # Why don't i use  a != None?  Because the method "findall" never returns None, it actualy returns a empty list of charac
            print(numbers)

    return None 

print(finding_numbers())
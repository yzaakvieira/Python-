import re 
reader = open("Python 2.1.txt", encoding = "utf-8")

def first_lines():

    for lines in reader:
        pattern = re.search("^Python", lines)

        if pattern != None:
            print(lines)
    return None


print(first_lines())


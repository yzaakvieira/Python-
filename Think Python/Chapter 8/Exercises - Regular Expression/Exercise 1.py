import re 
reader = open("Python 2.0.txt", encoding = "utf-8")

def read_print():

    for lines in reader:
        pattern = re.search("Python", lines)
        if pattern != None:
            print(lines)
    reader.close()


print(read_print())

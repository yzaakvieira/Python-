import re 
reader = open("Python 4.txt", encoding = "utf-8")

def cellphones():
    

    for lines in reader:
        pattern = re.search(r"\d{3}-\d{3}-\d{4}", lines)

        if pattern != None:
            print(pattern.group())
    return None

print(cellphones())



reader = open("pg345.txt", encoding = "utf-8")
writer = open('pg345_replaced.txt', "w", encoding = "utf-8")



def counting_firstway():
    total = 0
    for line in reader:
        if "Jonathan" in line: # Here we doesn't count the number of times a string appear in a sequence, just once.    
            total += 1
    return total

def counting_secondway():
    total = 0 
    for line in reader:
        total += line.count("Jonathan") # count returns the number of times a sequence appears in a string.
    return total
         


def replace():
    for line in reader:
        line = line.replace("Jonathan", "Thomas")
        writer.write(line)

print(replace())


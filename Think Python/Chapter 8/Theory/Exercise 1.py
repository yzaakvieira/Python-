reader = open("pg345.txt", encoding = "utf-8")
writer = open("exercise1.txt", "w", encoding = "utf-8")




def head(a):

    for i in reader:
        if len(i) >= 1:
            writer.write(i)
    
    
print(head(10))



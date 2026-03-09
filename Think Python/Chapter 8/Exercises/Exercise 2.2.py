"""See if you can write a function that does the same thing as the shell command !head - It's used to display the first few lines of a file, you can use the command. -
It should take as arguments the name of a file to read, the number of lines to read,
and the name of the file to write the lines into. If the third parameter is None, it
should display the lines rather than write them to a file."""


def head(file, number , filetowrite ):
    reader = open(file,"r", encoding= "utf-8")

    if filetowrite is not None: # First Restriction.
        writer = open(f"{filetowrite}.txt", "w",  encoding = "utf-8") # Opening the file to write in.

    for _ in range(number + 1): # The number of lines to write/print
        lines = reader.readline() # Reading each line.

        if filetowrite is None:
            print(lines, end = "")

        else:
            writer.write(lines)

    reader.close()
    if filetowrite is not None:
        writer.close()
    
    
    


print(head("Outer.txt", 50, "Inner" ))
    
# Nesse problema, meu maior aprendizado é:
# O primeiro passo quando não se sabe o primeiro passo é quebrar um problema complexo em partes muito menores, digo menores no sentido de ridiculamente fáceis, ou pelo menos, menos complexas que o problema original e ir aos poucos ir resolvendo  esses problemas, e de forma recursiva, podemos dizer assim; resolver o problema.

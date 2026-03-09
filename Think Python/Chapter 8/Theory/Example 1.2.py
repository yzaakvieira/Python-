

reader = open("pg345.txt", encoding = "utf-8")
writer = open('pg345_cleaned.txt', "w", encoding = "utf-8") # encoding = "utf-8" also works

def is_special_line(line):
    return line.startswith('***')


def the_last_first():
    for line in reader:
        if line.startswith("***"):
            print(line.strip()) # Strip é usado para ignorar os \n's no começo e no final de uma cadeia de caracteres, mas nunca no meio.

def break_line():
    for line in reader:
        if is_special_line(line):
            break

def writing():
    for line in reader:
        if is_special_line(line):
            break
        writer.write(line)




def writing_output():
    for line in reader:
        writer.write(line) # Que massa.



def check_end():
    for line in writer:
        line = line.strip()
        if len(line) > 0:
            print(line)
        if line.endswith('Stoker'):
            break

def first_lines():

    for line in open('pg345_cleaned.txt', encoding= "utf-8"):
        line = line.strip()
        if len(line) > 0:
            print(line)
        if line.endswith('Stoker'):
            break
        
# Estou sinceramente tendo alguns problemas, que pretendo fazer uma depuração depois:
# a função first_lines era para escrever algo como:
""" DRACULA
_by_
Bram Stoker""" # Mas essa função não está fazendo o desejado, mesmo chamando as funções para escrever o livro no arquivo cleaned antes. Apenas isso que está me gerando um problema, quero melhorar essa parte depois.

first_lines()
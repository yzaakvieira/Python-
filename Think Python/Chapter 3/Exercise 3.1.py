# Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display.
# Hint: use the len function, the string concatenation operator (+), and the string repetition operator (*).

# Eu acredito ter duas soluções para esse problema, a primeira usando os recursos citados pelo livro, e a segunda usando uma técnica de manipulação de strings, que eu pensei também em aplicar pro problema.

# The first one:

def print_right(a):
    spaced_nedeed = 40 - len(a)
    print((" ") * spaced_nedeed + a)
    # Aqui eu tentei fazer isso sem uma variável, mas estava dando um erro. Por isso a variável spaced(nedeed)


def print_right2(c):
    print('{:>40}'.format(f'{c}'))
    # Mas perceba que caso eu quisesse também poderia usar essa técnica de manipulação de strings. Entretanto como o problema diz para usarmos apenas concatenação, função len e  operador de repetição de strings a primeira função é a resposta correta - mas não a única.
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

print("\n")

print_right2("Monty")
print_right2("Python's")
print_right2("Flying Circus")


# Write a function called triangle that takes a string and an integer and draws a trianglewith the given height, made up of copies of the string. Here’s an example of a triangl with five levels using the string 'L':

i = input("Escreva uma letra: \n")
j = int(input("Escreva uma um número: \n"))
def triangle(a,b):
    for c in range(1, b + 1):
        print(a * c )

triangle("L",5)


print(triangle(i, j))
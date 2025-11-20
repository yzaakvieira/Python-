# 6. Construa um programa que leia do teclado e valide os seguintes dados sobre funcionários de uma empresa:
# a) Nome: maior que três caracteres.
#  b) Idade: entre 0 e 130.
#  c) Salário: maior que zero.
#  d) CEP: tamanho 8. 
# e) Departamento: ‘Administrativo’ ou ‘Fabrica’.

name = input("What's your name?")
if len(name) < 3:
    print("Oh... It needs more caracters please")

age = int(input("How old are you?"))

if age < 0 or age > 130:
 print("Hey, you're funny, but let's be real")

salary = int(input("How much money do you make per month?"))

if salary <= 0:
    print("Oh, are you a unemployee?")

zip = input("What is your ZIN code?")

if len(zip) != 8:
    print("Oh kid, that's wrong, try again")

departament = input("What is your departament?")

if departament != "Adminstrativo" or departament != "Fábrica":
    print("That's ok, everyone makes mistakes.")







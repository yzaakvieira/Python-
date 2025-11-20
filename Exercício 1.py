#  Crie um programa que solicite um número inteiro ao usuário e imprima na tela uma mensagem dizendo se o número é positivo ou negativo.
x = int(input("Digite um número inteiro:\n"))
print("O número digitado é positivo, que bom.") if x > 0 else print("O número digitado é negativo, sinto muito.")
# Utilizei um operador ternário, para facilitar a legibilidade.
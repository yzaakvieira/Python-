# Construa um programa em Python que solicite uma idade entre 0 e 130 anos. Imprima uma mensagem se o valor for inválido e continue solicitando até que o usuário digite um valor válido.
x = int(input("Digite uma idade entre 0 e 130 anos: \n"))
while (x < 0 or x > 130):
 x = int(input("Idade inválida, sinto muito, tente novamente:\n"))
print("Parabéns você acertou!")
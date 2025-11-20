# Crie um programa em Python que solicite ao usuário dois números inteiros e imprima o maior deles.
x = int(input("Digite o primeiro número:\n"))
y = int(input("Digite o segundo número:\n"))

print("\nO que acha de compararmos ambos? Vamos lá !\n")

if x > y:
    print("Temos um vencedor, o primeiro número: " + str(x))
else: 
    print("Temos um vencedor, o segundo número:" + str(y))
# Aqui eu poderia usar um operador ternário, para ficar mais enxuto, e legil, e também ter usado o f string. Mas de preferência, gostei  mais dessa sintaxe.




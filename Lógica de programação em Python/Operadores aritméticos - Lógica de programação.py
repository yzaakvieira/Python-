
import math
# Essa parte do código estarei testando o operador aritmético - Módulo - para verificar se um númeor possui valores
# Aqui estarei testando se um número ele possui resto 0 ou não 
print("Vamos verificar se um número ele possui resto em uma divisão: ")
numero_01 = int(input("Escreva o primeiro número para ser o dividendo: "))
numero_02 = int(input("Escreva o segundo número para ser o divisor: "))
modulo_teste = numero_01 % numero_02
print(f" Aqui está o resto da divisão: {modulo_teste}"  )
# % Mostra o resto da divisão
divisao_inteira = numero_01 // numero_02
print(divisao_inteira)
# // Mostra o quociente da divisão
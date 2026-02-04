# Calculando a média aritmética de um aluno, com o desvio condicional composto
primeira_nota = int(input("Escreva sua primeira nota: \n"))
segunda_nota = int(input("Escreva sua segunda nota: \n"))

nota = (primeira_nota * segunda_nota)/2

if nota >= 7:
    print("Você foi aprovado, meus parabéns")
else:
    print("Você infelizmente, não foi aprovado, sinto muito")
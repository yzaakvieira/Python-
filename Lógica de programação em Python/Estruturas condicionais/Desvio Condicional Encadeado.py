# O seguinte programa funciona assim: 
primeira_nota = int(input("Escreva sua primeira nota: \n"))
segunda_nota = int(input("Escreva sua segunda nota: \n"))

faltas = int(input("\nQuantas faltas você teve nesse bimestre?"))
nota = float((primeira_nota + segunda_nota)/2)

print(f"\nAqui está o resultado da sua nota: {nota}" )
print(f"\n Aqui está o quanto de faltas você acumulou esse bimestre: {faltas}")
if nota >= 7 and faltas < 10:
     print("Você foi aprovado, com excelência, meus parabéns.")
elif nota >= 5 and nota < 7 and faltas < 10:
    print("Você foi aprovado com uma nota média.")
else:
    print("Sinto lhe informar, mas você foi reprovado")



# Criar que nota o aluno deve tirar para obter ou a letra A (Nota excelente), nota B (Nota Mediana), nota C (Nota Baixa)

requisitos_notas = input("Para saber que nota é necessário A, B ou C, escreva quaisquer uma dessas letras: \n")

match requisitos_notas:
 case "A":
      print("\n Você precisa tirar entre 8 e 10")
 case "B":
      print("\nVocê precisa tirar entre 5 e 7")
 case "C":
      print("\nVocê precisa tirar abaixo de 5")
 case _:
      print("\nEssa letra não está entre as escolhidas")
     

print("\nAgora vamos calcular sua nota: ")

x = int(print("\nEscreva sua primeira nota: "))
y = int(print("\nEscreva sua segunda nota: "))
nota_bimestral = (x + y)/2



numero_01 = float(input("Escreva um número entre 0 a 10: "))
numero_02 = float(input("\nEscreva outro número de 11 a 20:  "))

if numero_01 >= 10 and numero_02 >= 20 and numero_02 <= 11:
 print(f"Aqui está a soma dos seu números {numero_01 + numero_02}")
else: 
 print("\nHey, está tentando fugir das regras do jogo?!")
 
    
print("\nAgora vamos somar 3 algarismos distintos, digite-os, sem trapacear hein!")

numero_03 = int(input("\nEscreva o primeiro algarismo: "))
numero_04 = int(input("\nEscreva o segundo algarismo:  "))
numero_05 = int(input("\nEscreva o terceiro algarismo:  "))

if numero_04 != numero_03 and numero_05 != numero_04:
 print(f" Aqui vai a soma dos 3 algarismos distintos: {numero_03 + numero_04 + numero_05}")
else:
 print("Opa, tentando trapacear de novo? Você merece uma surra de palmeiras, hein mocinho (a)")
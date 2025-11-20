print("Em rumo aos primeiros R$ 1000, vamos lá?!")
vlInvestido = int(input("Qual o valor que você tem investido nos últimos meses? \n"))
txInvestidos = int(input("Qual a taxa percentual que que você ganha no mês \n"))
x = int(input("Quantos meses você tem investido esse dinheiro: "))
total = (vlInvestido * x) * (txInvestidos/100) 
if total <= 1000:
 print(f"Então o capital acumulado foi: R${total}. Não desanime, estamos chegando quase lá :) ")
else:
 print(f"Então o capital acumulado foi: R${total}, Vamoos ! Todo sacrifício valeu a pena né? Meus parabéns pela conquista ! :)")
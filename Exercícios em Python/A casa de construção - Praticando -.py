metros = int(input("Quantos metros quadrados é a área? \n"))
caixa = (0.60*0.60*10)
total0 = int((metros / caixa))
print("Comprar caixas: " + str(total0))
print("Valor total da compra " + str(total0 * 70.00))

quantidade = int(input("\nQuantos cimentos você precisa?"))
total01 = quantidade * 33.00
print(total01)

n = int(input("Quantos a altura que você irá precisar?"))
p = int(input("Qual a largura você irá precisar?"))
largura = 2 
altura = 3 
if n < altura or  n > altura:
    print("Infelizmente, não estamos tendo esse modelo no momento")
elif  p < largura or n > largura:
    print("Olha, infelizmente, não estamos tendo esse modelo no momento - peço desculpas")

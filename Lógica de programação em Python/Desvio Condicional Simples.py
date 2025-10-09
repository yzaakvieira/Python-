# Calculando a nota de um estudante em duas provas e fazendo a média aritmética
nota = int(input("Escreva a sua nota na primeira prova: \n"))
nota_2 = int(input("Esreva a sua nota na segunda prova: \n"))
media_aritmetica= (nota + nota_2) / 2
# Aqui estamos diante um conceito praticado anteriormente que é a regra de precedência, porque, a precedência que prevaleceria, seria a divisão, mas como o parentêses tem precedência sobre a divisão, o que será calculado primeiro será a adição e não e divisão
print(f"Aqui está o seu resultado {media_aritmetica}")
if media_aritmetica >= 7:
    print("Você foi aprovado com excelência, meus parabéns!! :)")
if media_aritmetica <= 6 or media_aritmetica == 5 or media_aritmetica >= 6 and media_aritmetica < 7:
    print("Você foi aprovado, porém ficou na média")
if media_aritmetica < 5:
    print("Você infelizmente, não atingiu a nota necessária, portanto, foi reprovado")



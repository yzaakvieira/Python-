# O que significa Interpolação de Strings? É algo bem simples na real
# Interpolação de strings, é uma técnica de inserir variáveis ou expressões diretamente dentro de uma cadeia de caracteres (string); sem precisar ficar se preocupando em concatenar esses valores. É uma técnica simples, mas que torna o código mais legível
# Em Python temos 3 opções de fazer a interpolação em strings, a primeira que veremos é a mais antiga, com o uso do símbolo de porcentagem - % -, a outra é com .format(), e por último a print(f" ") que é a mais simples de todas, bora?!

a = int(input("Escreva um dígito, para fazermos uma suposição:\n"))

print(f"\nEntão você possui{a} anos de idade.\n")

print("Então o calçado do seu pé é %i.\n" % (a))

print("O primeiro seriado animado que você assistiu com {} anos, foi 'A hora da aventura' ?".format(a))

print("Você conheceu o amor da sua vida com {amor} anos".format(amor=a))
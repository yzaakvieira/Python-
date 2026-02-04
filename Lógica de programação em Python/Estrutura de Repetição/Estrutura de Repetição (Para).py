# O que é a estrutura para? e para que ela serve? Bem são perguntas que podem surgir, então vamos lá...
# A estrutura para ela serve para quando sabemos quantas vezes iremos iterar um bloco de códigos, sejam 10 10.000 ou até mesmo 10.000.000, mas a noção aqui é, essa iteração ela é finita, aí o para (Ou for) entrar
# A sintaxe dessa estrutura em pseudo-código é a seguinte:
# para variável (início, fim, passo)
# para - Início da nossa estrutura -, variável  - É a variável contadora -, (...) - São os parâmetros que essa função receberá -, início - Onde se inicia a nossa sequência finita -, fim - Onde ela oBviAmEntE termina kk - e o passo seria o valor para incrementar a variável a cada loop
# Exemplo:


N = int(input("Digite o valor de N: "))
fat = 1

print(f"\nCalculando {N}! passo a passo:\n")

for contador in range(1, N + 1):
    print(f"{fat} × {contador} = {fat * contador}")
    fat = fat * contador  

print(f"\nO fatorial de {N} é {fat}")
















a = "Charles"
n = len(a)

for i in range(n):
    print(a[i]) 

# Em strings podemos acessar os elementos code points usando um índice e é usada a notação "variavel[ index ]". O índice varia de 0 até o tamanho da string menos 1. Se ele for negativo, a contagem é na ordem inversa -  Começa em -n (último caracter) e a depender do tamanho da string continuará até acabar os caracteres

# Ou


print ("\n")
for i in range(-n, 0):
    print(a[i])

# string_1 = "Piracicabana"
# string_1[9] = "o" 
# A maneira acima dá um erro, pois o Python não suporta a mudança de um caracter em uma string dessa maneira.
string_1 = "Piracicabana"
string_1 = string_1[0:11] + "o"
# Aqui é um jeito, posso pegar o intervalo de 0 a 11 e como vai faltar um caracter, concatenar com o caracter que eu queira.
print(string_1)
string_2 = "Paralelepido"
string_2 = string_2.replace("e", "a")
print(string_2)
#Perceba que ele troca todas as strings que contenham o primeiro parâmetro, pelo segundo elemento.

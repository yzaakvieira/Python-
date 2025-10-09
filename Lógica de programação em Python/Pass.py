# Uma peculiaridade do Python, é que as estruturas condicionais, tenham pelo menos uma instrução, mas e se caso, eu quiser deixar para escrever a instrução depois? Bem eu posso usar o pass que é uma instrução vazia, ou seja, ela não executa nada. E isso evita que o Python, puxe a sua orelha por não ter colocado uma instrução logo após a condição. Vamos ver um exemplo prático:
a = 50
b = 170
if a > 100:
 pass
else:
 pass
# Perceba, que se eu quiser, depois eu consigo inserir a instrução, assim fica mais fácil, e mais eficiente, caso eu precise fechar a minha IDE, e e queira deixar as minhas estruturas condicionais prontas para uso posterior.
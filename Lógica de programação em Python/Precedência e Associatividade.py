# Aqui eu irei praticar o uso de conceitos como Precedência - Ordem que os operadores adjacentes são processados em uma expressão - e a Associatividade - A ordem na qual operadores com a mesma ordem de precedência são executados (Direita - Esquerda ou Esquerda - Direita)
a = int(input("Escreva o primeiro número: \n"))
b = int(input("Escreva o segundo número: \n"))
c = int(input("Escreva o terceiro número: \n"))
d = int(input("Escreva o quarto número: \n"))
e = int(input("Escreva o quinto número: \n"))
(print(f"Vamos somar e subtrair { a + b - c + d - e}"))
# Aqui está a associatividade aplicado na prática, nesse caso a ordem de precedência dos operadores é igual, porém a sua associatividade - A ordem de prioridade, que leva em conta não apenas o operador, mas sim a posição na qual ele se encontra, é como se fosse um conceito em matemática chamado "algarismo relativo" que leva em conta não o algarismo absoluto, mas sim a posição na qual ele se encontra. Isso é, quando não temos um parentêses na expressão, porque a partir daí, a precedência entra em ação.
# Vamos fazer um exemplo, com os mesmos operadores:
(print(f"\nVamos somar e subtrair { a + b - (c + d) - e}"))
# Aqui é um exemplo interessante, pense o seguinte, primeiro eu mudei a ordem precedência, colocando o parentêses, após isso entra a regra de associativade, ou seja - Nesse caso as operações seguintes serão feitas da esquerda para direita - a + b será executado primeiro, pela regra de associatividade que nesse caso é da esquerda para direita, depois será subtraido pela soma de c + d, e por fim, será subtraído  - e.
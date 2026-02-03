# Em python, existem duas maneiras diferentes de saber qual o tipo de um objeto/classe
# De maneira direita tem a função "type()", que retorna dado um parâmetro o tipo de um objeto
# Uma maneira também muito interessante, que o python tem é a função "isinstance()", que geralmente é usada em conjunto com uma estrutura condicional, ou mais chique: "simple conditional branch" kk. De qualquer forma, eu achei uma maneira bastante elegante.
# E perceba que por Python ser uma linguagem de programação dinâmica - significa que as conversões de tipos de dados é feita em tempo de execução -, os dados podem mudar de tipo durante a execução do programa e aí precisamos, ás vezes, saber o tipo do dado de um objeto. 
a = float(input("Digite um número qualquer: \n "))
print(f"Oras, verifiquei aqui e você digitou um dado do tipo: {type(a)} ")

if isinstance(a,int):
    print("Oras, se trata de um int; bem o que esperava.")
else:
    print("Oras, esperava que fosse um int, mas tudo bem. ")

# A minha proposta, seria criar um programa no qual, enquanto a pessoa não acertar o número "escondido" se repete a variável "a", solicitando para que a pessoa escreva outro  número
# Outra coisa interessante de implementar é criar um escopo, por exemplo se a quantidade de números for até 100 e meu número é 77, e a pessoa digita 50 aparece na tela "Esse número está abaixo do escondido", se ela digitar 80 aparece "Hm... Quase lá, está bem perto, mas ainda não é esse número"



numero_secreto = 47
# Essa variável é o número "escondido" do usuário, ou seja, o número que ele está tentando acertar
a = int(input("Escreva um número de 0 à 100, e descubra o número secreto... \n"))
# Essa variável é o primeiro número que ele vai digitar

while (a != numero_secreto):
    # Tá... Mas para que serve o while? Ele é uma ferramente de Iteração - Um processo repetido até chegar em um resultado - Nesse caso eu tenho os parâmetros - As condições - e tenho bloco de código que será executado, e caso a minha condição seja falsa, ele encerra o bloco do while, e segue para próxima instrução que está fora da indentação do while. Bem maneiro né?! :)
    if a < numero_secreto:
        print("Esse  número é abaixo do nosso número :( ")
    elif a > numero_secreto:
        print("Esse número excede o nosso número")
    print("\n Vamos lá, não desanime, tente novamente")
    a = int(input("\n Mais uma chance, tente novamente:  \n"))
    # Aqui é interessante frizar que por python ele ser fortemente e dinâmicamente tipado (Principalmente dinâmicamente tipado), eu posso atribuir um valor a uma variável, e depois modifica-la durante o meu programa, porque ele converte o valor atribuido a variável em tempo de execução do programa.
print("Aeee !!! É esse número, meus parabéns")
 
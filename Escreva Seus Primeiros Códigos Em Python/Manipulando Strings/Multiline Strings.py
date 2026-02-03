# O que são multiline strings?
# Multiline strings: São strings que podem abranger mais de uma linha de texto. Em vez de ser limitado a uma única linha, eles permitem que você escreva o texto exatamente como ele aparece, incluindo quebras de linha.
# Para usa-los, usaremos a notação: """ obj """ ou ''' obj '''. Ou seja por 3 aspas duplas, ou então por 3 aspas simples.


print('''             Não tenho pressa - Fernando Pessoa
     Não tenho pressa. Pressa de quê?
     Não têm pressa o sol e a lua: estão certos.
     Ter pressa é crer que a gente passa adiante das pernas,
     Ou que, dando um pulo, salta por cima da sombra.
     Não; não sei ter pressa.
     Se estendo o braço, chego exactamente aonde o meu braço chega -
     Nem um centímetro mais longe.
     Toco só onde toco, não aonde penso.
     Só me posso sentar aonde estou.
     E isto faz rir como todas as verdades absolutamente verdadeiras,
     Mas o que faz rir a valer é que nós pensamos sempre noutra coisa,
     E vivemos vadios da nossa realidade.
     E estamos sempre fora dela porque estamos aqui.
 ''')
# Também é possível fazer o mesmo processo com o \n para quebrar as linhas, mas essa maneira é mais legível.

print('Olá mundo ' 
      'Como vai?')
# É possível quebrar strings longas que não sãomultiline apenas ao quebrar a linha, de preferência indentando-as.
# Qual a diferente entre print('Olá mundo " "Como vai?") e print('Olá mundo" "Como vai?"). Simplesmente o espaço após o mundo, não por que a segunda string está identada, isso serve apenas para visualização, não possui nenhum efeito real sobre a separação das strings.
print('Em qual cidade o legado da Copa foi mais relevante ' 'para a populacao?')
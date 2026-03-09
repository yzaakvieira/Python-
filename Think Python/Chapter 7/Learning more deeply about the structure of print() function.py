for i in range(3):
    print(i, end=' ') # end = keyword argument used in the print()  | keyword arguments: An argument that includes the name of the parameter  - Keyword arguments are named parameters passed to functions in programming (especially in Python), allowing values to be specified out of order.| 

    # This version uses the keyword argument end, so the print function puts a space after each number rather than a newline.
     # Estranho esse "end", não? Bem esse end é um parâmetro da função print, que por padrão a estrutura é:

    # print(*objects, sep=' ', end='\n', file=None, flush=False) apenas mudamos a quebra de linha por um espaço.

    # sep → separador entre valores

    # end → o que é impresso no final

    # file → onde imprimir

    # flush → controle de buffer -> buffer: Um espaço temporário onde dados ficam guardados antes de serem enviados para outro lugar. | Flush: Esvaziar o buffer (forçar o envio imediato do que está armazenado).  

    # At the first moment, i couldn't remember what was a keyword argument, and then it helped me not only remember, but learn more deeply about the structure of the print() function. At first i thought the end would be a a local variable, but it doesn't xd
3""" Write a function named uses_none that takes a word and a string of forbidden letters,
and returns True if the word does not use any of the forbidden letters.
"""
from doctest import run_docstring_examples 

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__, )

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for forbidden_letters in word.lower():
        if  forbidden_letters in forbidden.lower():
            return False
    return True # Isso funciona porque na primeira letra que estiver em forbidden, temos um valor de retorno, e imediatamente a função se encerra. Com isso for loop, ele continuará iterando até a última letra, e por isso essa parte funciona, a função irá retornar verdadeiro, somente se o primeiro ramo for falso, e aí retorna True e encerra o programa, perceba que, como o return encerra a função imediatamente, não poderiamos fazer com um not operator e etc - Como eu tentei fazer anteriormente kk.
        
run_doctests(uses_none)
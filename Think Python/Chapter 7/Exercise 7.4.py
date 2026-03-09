""" The New York Times publishes a daily puzzle called “Spelling Bee” that challenges
readers to spell as many words as possible using only seven letters, where one of the
letters is required. The words must have at least four letters.
For example, on the day I wrote this, the letters were ACDLORT, with R as the
required letter. So “color” is an acceptable word, but “told” is not, because it does not
use R, and “rat” is not because it has only three letters. Letters can be repeated, so
“ratatat” is acceptable.
    -> Write a function called check_word that checks whether a given word is acceptable. It
    should take as parameters the word to check, a string of seven available letters, and a string containing the single required letter. You can use the functions you wrote in
    previous exercises. """
from doctest import run_docstring_examples 

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__, )

def uses_only(word, avaiable):
    """Checks whether a word uses only the available letters.
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for _ in word.lower():
        if _ not in avaiable.lower():
            return False
    return True


def uses_all(word, required):
    """Checks whether a word contains all required letters. 
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False   
    """
    for letter  in required.lower():
        if  letter not in word.lower():
            return False
    return True


def check_word(word, available, required):
    """Check whether a word is acceptable.
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) >= 4 and len(available) == 7: # Escolhi usar uma condicional aninhada, e acho que pro exercício, fez o esperado, pois a palavra poderia cobrir todos os parâmetros abaixo, porém se fosse menor do que 4 ela retornaria false, se as letras disponíveis fossem menores que 7 o programa também retornaria falso.
        if uses_only(word, available) == True and uses_all(word, required) == True:
            return True
        return False
    return False

run_doctests(check_word)
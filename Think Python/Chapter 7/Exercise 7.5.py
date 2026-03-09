
# Write a function called uses_all that takes a word and a string of letters, and that returns True if the word contains all of the letters in the string at least once.

from doctest import run_docstring_examples 

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__, )


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




def word_score(word, available):
    """Compute the score for an acceptable word.
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    
    word = word.lower()
    available = available.lower()

    # Base score
    if len(word) == 4:
        score = 1
    else:
        score = len(word)

    # Pangram bonus
    if uses_all(word, available):
        score = score + 7

    return score
    

run_doctests(word_score)
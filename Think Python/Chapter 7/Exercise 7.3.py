    # Write a function called uses_all that takes a word and a string of letters, and that returns True if the word contains all of the letters in the string at least once.

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

run_doctests(uses_all)
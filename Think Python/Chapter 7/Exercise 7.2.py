    # Write a function called uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the string.
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

run_doctests(uses_only)

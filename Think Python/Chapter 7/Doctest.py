from doctest import run_docstring_examples 

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__, )
 # Here besides the example above, i could use a kerword argument called "verbose = True" which it would give me a very detailed description at the test.   Verbose: Na computação e tecnologia, indica um modo que fornece informações detalhadas e abrangentes sobre o processo em andamento, sendo útil para depuração e monitoramento técnico. 
def uses_any(word, letters):
    """Checks if a word uses any of a list of letters.
    >>> uses_any('banana', 'aeiou')    
    True
    >>> uses_any('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False




def uses_any_incorrect(word, letters):
    """Checks if a word uses any of a list of letters.
    >>> uses_any_incorrect('banana', 'aeiou')
    True
    >>> uses_any_incorrect('apple', 'xyz')
    False
    """
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False # INCORRECT!
        # Why this second version is incorrect? You could actually notice that the first one doesn't have the else, and expect that the else is the problem, but it doesn't. The main problem here is the "return" statement, because it ends the function and returns a value immediately, so after that, everthing stops, and if there's some code after it; it becomes dead code.
    
run_doctests(uses_any)

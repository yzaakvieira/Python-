# -> We can actually make the has_e function we have written even better, with the in operator, that checks whether a character appears in string or not. The in operator returns a boolean value, so it isn't  necessary use a contidional to test it.


def has_e1(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False

def has_e(word):
    return 'e' in word.lower()
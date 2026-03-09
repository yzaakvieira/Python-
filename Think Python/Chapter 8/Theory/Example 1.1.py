def compare_word(word):
    if word.lower() < 'banana':
        print(word, 'comes before banana.')
    elif word.lower() > 'banana':
        print(word, 'comes after banana.')
    else:
        print('All right, banana.')

a = input("Write a word: \n")

print(compare_word(a))

# This coding is working because the relational operator is comparing the unicode by unicode of the string, for example apple and banana, the unicode of a is less than b, so a comes first, and so on, for any number of characters.
# -> Python does not handle uppercase and lowercase letters the same way people do. All the uppercase letters come before all the lowercase letters. Which is caused by the unicode.

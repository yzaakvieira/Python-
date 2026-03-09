


# Aqui no futuro, uma melhora seria: Tentar importar o módulo "Example 2", e então usar a função has_e desse arquivo .py. Por enquanto, como sei bem pouco sobre o assunto, reutilizar a função nesse arquivo foi o melhor que pude fazer.

def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False

def words():
    total = 0
    count = 0
    for line in open('words.txt'):
        word  = line.strip() 
        
        print(word)
        total += 1
        if has_e(word):
            count += 1

    print(total, count)
    print(count/total * 100)

print(words())


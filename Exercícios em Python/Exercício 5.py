# 5. Crie um programa que verifique se uma letra digitada pelo usuário é uma vogal, consoante ou número.


print("Hey! Hello, how are you? Let's make game. If i can discover what's the thing that you'll write down here, let's begin !")

letter = input("Hey, first things first, give me a number, consonant or a vowel: \n")
if letter in ["0", "1","2", "3" "4", "5", "6", "7", "8", "9"]:
    print("Uepa, that's a number, isn't it?")
elif letter in ["a", "e", "i", "o", "u"]:
    print("UePa, is it a vowel, isn't it?")
else:
    print("You're smart, but not enough. Is this a consonant, right? HAHAHA")
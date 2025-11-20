#  Faça um programa que solicite o nome do usuário e a senha, imprimindo uma mensagem de erro e voltando a solicitar uma nova senha caso ela seja igual ao nome do usuário.
name = input("What is your first name?\n")
password = input("What'll be your password?\n")
while name == password:
 print("\nUepa, it seems something is wrong here, isn't? Your name is the same as the password, try again please :)")
 password = input("\nWhat'll be your password?\n")
print("That's right, thanks for the information, have good time, and take care. Byee ! ")
    

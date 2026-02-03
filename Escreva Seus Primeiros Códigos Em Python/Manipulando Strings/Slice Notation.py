# Aqui tentarei usar as slices notations (notações em pedaços)
# Elas servem para literalmente despedaçar uma string em fatias. Quantas fatias? Quantas quisermos. Quais fatias? Quais quisermos. Vamos testar algumas delas
a = "Paralelepido"
print(a[0:3])
# Aqui eu quero que você perceba algo, em Python, a sintaxe será: variável[start:stop]. Nessa sintaxe teremos variações - logo a seguir. Mas por enquanto, perceba que se formos de 0 até 3 o output correto seria: "Para". Mas como deves ver a output foi: "Par". Nesse caso em Python sempre será subtraído 1 de stop, então ficaria algo assim: variável[start:stop-1]
print(a[4:])
print(a[:8])
print(a[:])
print(a[::2])
# Assim como no for; em Python a slice notation também tem início, fim, passo, a sintaxe completa então ficaria: variavel[start:stop:step]
print(a[0:8:2])

print("""Para mais informações sobre a Slice Notation, um ótimo artigo será da StackOverFlow:
      https://stackoverflow.com/questions/509211/how-slicing-in-python-works""")

# Um fato interessante sobre as slices notations, é que elas também podem ser usadas com listas, o que as tornam muito úteis.
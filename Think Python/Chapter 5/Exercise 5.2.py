
# If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are 1 inch long,
# you will not be able to get the short sticks to meet in the middle.

# For any three lengths, there is a test to see if it is possible to form a triangle:

# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle.
# Otherwise, you can.

# (If the sum of two lengths equals the third, they form what is called
# a “degenerate” triangle.)

# Write a function named is_triangle that takes three integers as arguments,
# and that prints either “Yes” or “No,” depending on whether you can or cannot
# form a triangle from sticks with the given lengths.

# Hint: use a chained conditional.




values = [] # Lista para armazenar os valores do laço for
for _ in range(3): # Iteração de 3 vezes. _ foi usado pois não foi utilizado durante a iteração
    z = int(input("Digite um valor para formamos o nosso triangulos\n"))
    values.append(z) # Adicionando os valores de z na lista


def is_triangle(a,b,c): # Globalização da função

    if a >= c + b or b >= c + a or c >= a + b: # Desigualdade triangular 
        print( f"No")
    
    else: 
        print("Yes")

    # Também poderia usar uma chained conditional, mas assim dessa maneira, fica mais enxuto, com menos branches.
        

is_triangle(*values) # Desempacotei os valores da lista como argumento na função


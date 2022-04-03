"""7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetise ningún elemento en la nueva lista:"""

lista_1 = ["J",'e','s','s',' ', 'C','r','i','s']
lista_2 = ["J",'e','s','y',' ', 'A','n','i']

lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)
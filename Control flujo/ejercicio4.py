"""4) Realiza un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética:"""

suma = 0
numeros = int(input("¿Cuántos números quiere introducir? "))
for x in range(numeros):
    suma += float(input("Introduce un número: "))
print("Se han ingresado",numeros,"números en total y la media aritmética es",suma/numeros)
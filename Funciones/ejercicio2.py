"""2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

Nota: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

import math
print(math.pi)
> 3.1415..."""

import math   #importar función matemática
pi = math.pi

def circulo(radio):
    area = pi*radio**2
    print("Él área de un círculo es", round(area,2))
circulo(5)
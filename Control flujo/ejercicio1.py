"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 menues en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""

a = float(input("Ingresar el primer número: ") )
b = float(input("Ingresar el segundo número: ") )

menu = 0           
print("¿Qué quieres hacer? \n1) Sumar los dos números. \n2) Restar los dos números. \n3) Multiplicar los dos números.")
menu = int(input("\nEscoja un numero dentro del menú: ") )     

if menu == 1:
    print("La suma de",a,"+",b,"es",a+b)
elif menu == 2:
    print("La resta de",a,"-",b,"es",a-b)
elif menu == 3:
    print("El producto de",a,"*",b,"es",a*b)
else:
    print("Ingrese opción válida")
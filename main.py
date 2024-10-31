#Exercise 5. Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

#Ingrese numero: 51
#Ingrese numero: 24
#24 51
#
# A continuación, escriba otro programa que haga lo mismo con tres números:
#
#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
#
# Finalmente, escriba un tercer programa que ordene cuatro números:

#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
#0 1 6 7

#Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí.
#Hay más de una manera de resolver cada ejercicio.

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

if number1 <= number2 and number1 <= number3:
    minor = number1
    if number2 <= number3:
       middle, major = number2, number3
    else:
        middle, major = number3, number2
elif number2 <= number1 and number2 <= number3:
    minor = number2
    if number1 <= number3:
        middle, major = number1, number3
    else:
        middle, major = number3, number1
else:
    minor = number3
    if number1 <= number2:
        middle, major = number1, number2
    else:
        middle, major = number2, number1

print(minor, middle, major)

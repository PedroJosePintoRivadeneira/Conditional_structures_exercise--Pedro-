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

if number1 < number2:
    print(number1, number2)
else:
    print(number2, number1)

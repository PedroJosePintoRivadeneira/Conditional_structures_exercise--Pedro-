#Exercise 1. Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

#Ingrese un número: 4
#Su número es par
#Ingrese un número: 3
#Su número es impar

number = int(input("Enter a number "))

if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
    
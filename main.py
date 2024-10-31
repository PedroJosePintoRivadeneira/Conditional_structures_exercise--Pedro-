#Exercise 6. Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
# En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.

#Ingrese caracter: A
#Es letra mayúscula.

#Ingrese caracter: f
#Es letra minúscula.

#Ingrese caracter: #
#No es letra ni número.

character = input("Enter a character: ")

if "0" <= character <= "9" :
    print("It's a number.")
elif "A" <= character <= "Z" :
    print("It's is an uppercase letter.")
elif "a" <= character <= "z" :
    print("It's a lowercase letter.")
else:
    print("It's neither a letter not a number.")

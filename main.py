#Exercise 8. Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos
#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011
#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.

from time import localtime

t = localtime()
current_day = t.tm_mday
current_month = t.tm_mon
current_year = t.tm_year

birth_day = int(input("Enter your birth date.\nDay: "))
birth_month = int(input("Month: "))
birth_year = int(input("Year: "))

age = current_year - birth_year

if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    age -= 1

print(f"You are {age} years old.")

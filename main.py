#Exercise 3. Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es 
# exacta o no.

#Dividendo: 14
#Divisor: 5
#La división no es exacta.
#Cociente: 2
#Resto: 4

#Dividendo: 100
#Divisor: 10
#La división es exacta.
#Cociente: 10
#Resto: 0

dividend = int(input("Dividend: "))
divider = int(input("Divider: "))

quotient = dividend // divider
remains = dividend % divider

if remains == 0:
    print("The division is exact.")
else:
    print("The division isn't exact.")

print(f"Quotient: {quotient}")
print(f"Remains: {remains}")

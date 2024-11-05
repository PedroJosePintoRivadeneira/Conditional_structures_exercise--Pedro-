#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los 
# lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.

# Ingrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.

#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.

#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0
#El triangulo es escaleno.
# Input for the sides of the triangle

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a <= 0:
    print("It is not a valid triangle.")
elif b <= 0:
    print("It is not a valid triangle.")
elif c <= 0:
    print("It is not a valid triangle.")
else:
    if a + b <= c:
        print("It is not a valid triangle.")
    elif a + c <= b:
        print("It is not a valid triangle.")
    elif b + c <= a:
        print("It is not a valid triangle.")
    else:
        if a == b and b == c:
            print("The triangle is equilateral.")
        elif a == b or a == c or b == c:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
            
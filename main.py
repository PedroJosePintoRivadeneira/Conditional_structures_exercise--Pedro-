#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y 
# división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5

#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1

#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20

#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5

#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

operand1 = float(input("Operand: "))
operator = input("Operator (+, -, *, /): ")
operand2 = float(input("Operand: "))

if operator == "+" :
    result = operand1 + operand2
    print(f"{operand1} + {operand2} = {result}")
elif operator == "-" :
    result = operand1 - operand2
    print(f"{operand1} - {operand2} = {result}")
elif operator == "*" :
    result = operand1 * operand2
    print(f"{operand1} * {operand2} = {result}")
elif operator == "/" :
    if operand2 != 0 :
        result = operand1 / operand2
        print(f"{operand1} / {operand2} = {result}")
    else:
        print("Error: Division by zero.")
else:
    print(f"Error: Invalid operator '{operator}'. ")

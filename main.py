#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

# 	edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición 
# de riesgo.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
year = int(input("Enter your age in years: "))

imc = weight / (height ** 2)

if year < 45:
    if imc < 22.0:
        risk = "low"
    else:
        risk = "medium"
else:
    if imc < 22.0:
        risk = "medium"
    else:
        risk = "high"

print(f"""
      Your body mass index (BMI) is: {imc}
      Your risk condition is: {risk}
""")

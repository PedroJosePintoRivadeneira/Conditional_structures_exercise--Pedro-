#Exercise 4. Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por 
# cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.

#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol

#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo

word1 = str(input("Word 1: "))
word2 = str(input("Word 2: "))

large1 = len(word1)
large2 = len(word2)

if large1 > large2:
    difference = large1 - large2
    print(f"The word {word1} has {difference} more letters than {word2}")
elif large2 > large1:
    difference = large2 - large1
    print(f"The word {word2} has {difference} more letters than {word1}")
else:
    print("The two words have the same length")
    
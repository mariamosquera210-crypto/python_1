"""
#ciclo for = repite por cantidades de
for i in range(10):
    print(f"{i} Hola Mundo.")"""

""""
configurar posicion inicila y final 
for i in range(1, 11):
    print(f"{i} Hola Mundo.")

    """
"""
for i in range (2,12,2):
    print(f"{i}. Hola Mundo.")
"""

"""
for i in range (1,105,5):
    print(f"{i}. Hola Mundo.")

"""
""""
import random

numero_secreto = random.randint(1,10)
intentos= 3

for i in range (intentos): #Ciclo para que se escriba varias veces
    numero = int(input("Adivina el numero secreto (1-10):"))

    if numero == numero_secreto:
        print("felicidades Adivinaste.")
        break
    else:
        intentos_restantes = intentos - (i + 1)
                           #3 - (8+1) = 2

print(f"❌te queda { intentos} intentos")

#verificar si no quedan intentos y mostrar el numero
if intentos_restantes
    print(f"😲 lo siento, el numero secreto era:")
"""

#Ejercicio 1. 

for i in range(1,11):   # recorre los valores del 1 al 10
    print(f"{5} X {i} = { 5* i}")
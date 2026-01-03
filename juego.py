import random

print("🎮 Bienvenido al juego Adivina el Número")
print("Estoy pensando en un número del 1 al 5")

numero_secreto = random.randint(1, 5)

intento = input("Adivina el número: ")
intento = int(intento)

if intento == numero_secreto:
    print("🎉 ¡Ganaste! Adivinaste el número")
else:
    print("😅 No acertaste")
    print("El número era:", numero_secreto)

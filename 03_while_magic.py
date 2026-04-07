#The goal in this algorithm is to complete it until the user guess the secret number
secret_number = 777


print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero=(int(input("Ingrese un numero entero: \n")))

while numero != secret_number:
    print("Ja, ja, Estás atrapado en mi bucle")
    numero=(int(input("Inserta de nuevo un número: \n")))

print("Muy bien, eres libre")





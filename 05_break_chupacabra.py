# En este algoritmo el usuario debe de ingresar palabras, si ingresa la palabra chupacabra sale del ciclo

print("Bienvenido al programa de escribir una palabra")
palabra = str(input("Ingrese la palabra"))

while palabra != 'chupacabra':
    palabra = str(input("Ingrese la palabra: \n"))
    if palabra == 'chupacabra':
        print("Has salido del bucle")
        break
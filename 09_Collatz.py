print("Bienvenido al programa de la hipótesis de Collatz \n")

c0 = int(input("Ingrese un numero entero positivo: \n"))
pasos = 0

if c0 != 0:
    while c0 != 1:
        if c0 %2 == 0:
            c0 = c0 // 2   #Doble diagonal para que el resultado sea entero
            pasos = pasos + 1
        else:
            c0 = 3 * c0 + 1
            pasos = pasos +1
        print(c0)
    print("El numero de pasos es:", pasos)
    
else:
    print("No puede ingresar el 0")

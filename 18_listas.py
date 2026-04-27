#escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
#escribir una línea de código que elimine el último elemento de la lista (Paso 2)
#escribir una línea de código que imprima la longitud de la lista existente (Paso 3).


hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

print("Bienvenido al porgrama de listas \n")
num= int(input(("Ingrese el numero por el que quisiera reemplazar el numero de enmedio de la lista: \n")))

hat_list[2] = num

print(hat_list)

#Eliminar el ultimo elemento de la lista
del hat_list[-1]
print(hat_list)

#La longitud de la lista

print(len(hat_list))
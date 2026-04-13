# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

print("Bienvenido al devorador de vocales")
user_word = str(input("Ingrese una palabra: \n"))

user_word = user_word.upper() #La cadena se poner en mayusculas

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print("Las letras sin devorar es: \n", letter)

    
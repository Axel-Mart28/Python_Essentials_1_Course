#Ahora se van concatenando las letras

word_without_vowels = ""

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
        word_without_vowels = word_without_vowels + letter
        print(word_without_vowels)

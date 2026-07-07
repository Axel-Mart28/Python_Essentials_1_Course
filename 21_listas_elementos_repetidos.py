#En este programa el usuario debe ingresar números, los que no estén en my_list se van agregando a la lista, los que ya esten, se ignoran

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #Lista original
lista_temporal = [] #Lista temporal

for valor in my_list:
    if valor not in lista_temporal:
        lista_temporal.append(valor)
    
my_list = lista_temporal[:]

print("La lista con elementos únicos:")
print(my_list)
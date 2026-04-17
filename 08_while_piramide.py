print("Bienvenido al programa de piramides")

blocks = int(input("Ingresa el número de bloques: "))

altura_inicial = 0
capa_por_bloques = 1

while capa_por_bloques <= blocks:
    blocks = blocks - capa_por_bloques

    altura_inicial = altura_inicial + 1
    
    capa_por_bloques = capa_por_bloques + 1

print("La altura de la pirámide:", altura_inicial)
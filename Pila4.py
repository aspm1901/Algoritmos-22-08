pilaFia = []
pilaFia2 = []

# Push inicial
for i in range (1,16):
    pilaFia.append(i)

print("Pila inicial:", pilaFia)

# Conjunto de números a eliminar
sacarT=3
sacarD=7
temp = 0

# Sacar elementos hasta vaciar la pila
while pilaFia:
    temp = pilaFia.pop()
    if temp == sacarD or temp == sacarT:
        print(f"¡Número {temp} eliminado!")
        # No se guarda en pilaFia2
    else:
        pilaFia2.append(temp)

print("Pila después de eliminaciones (vacía temporalmente):", pilaFia)
print("Elementos guardados temporalmente:", pilaFia2)

# Restaurar elementos en el orden original
while pilaFia2:
    pilaFia.append(pilaFia2.pop())

print("Pila restaurada (sin los números eliminados):", pilaFia)
pilaFia = []

# Ingresar nombres 
for i in range(20):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    pilaFia.append(nombre)

print("\nPila inicial:", pilaFia)

eliminados = []

# LIFO: elimina el último ingresado
if pilaFia:
    eliminados.append(("LIFO", pilaFia.pop()))

# FIFO: elimina el primero ingresado (de la misma lista)
if pilaFia:
    eliminados.append(("FIFO", pilaFia.pop(0)))

print("\nEliminados:")
for modo, nombre in eliminados:
    print(f" - {modo}: {nombre}")

print("\nPila final:", pilaFia)
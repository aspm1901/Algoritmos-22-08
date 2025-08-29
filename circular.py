class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.rear = -1
        self.tamaño = 0

    def enqueue(self, elemento):
        if self.isFull():
            return "La cola está llena"
        self.rear = (self.rear + 1) % self.capacidad
        self.cola[self.rear] = elemento
        self.tamaño += 1

    def dequeue(self):
        if self.isEmpty():
            return "La cola está vacía"
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  # Limpia el espacio
        self.frente = (self.frente + 1) % self.capacidad
        self.tamaño -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            return "La cola está vacía"
        return self.cola[self.frente]

    def isEmpty(self):
        return self.tamaño == 0

    def isFull(self):
        return self.tamaño == self.capacidad

    def size(self):
        return self.tamaño

    def mostrar(self):
        return self.cola

# Crear una cola circular con capacidad 5
cola = ColaCircular(5)

cola.enqueue('Aldo')
cola.enqueue('Bianca')
cola.enqueue('Carlos')
print("Cola:", cola.mostrar())
print("Primer elemento:", cola.peek())
print("Eliminar:", cola.dequeue())
print("Cola después de eliminar:", cola.mostrar())
print("Está vacía:", cola.isEmpty())
print("Está llena:", cola.isFull())
print("Tamaño:", cola.size())

# Agregar más elementos
cola.enqueue('Diana')
cola.enqueue('Elena')
cola.enqueue('Fernando')  # Llenará la cola
print("Cola llena:", cola.mostrar())
print("Agregar más:", cola.enqueue('Gustavo'))  # Debería mostrar que está llena

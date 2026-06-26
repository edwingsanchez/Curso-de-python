#Las pilas y las colas son estructuras de datos lineales que organizan la información de manera secuencial. 
# La diferencia principal radica en el orden en que manejan sus elementos y los extremos que utilizan:
# Colas (Queues): Utilizan el principio FIFO (First In, First Out). El primer elemento en entrar es el primero en salir.
# Pilas (Stacks): Utilizan el principio LIFO (Last In, First Out). El último elemento que se añade es el primero en ser retirado.
from collections import deque



#COLA
productosCarrito = deque(["Leche", "Arroz", "Pescado", "Tomate"])

print ("Carrito: ", (list(productosCarrito)))

Escaneado = productosCarrito.popleft()

print("Producto escaneado:", Escaneado)

print(f"Productos Restantes: {list(productosCarrito)}")


#PILA
productosCarrito = (["Leche", "Arroz", "Pescado", "Tomate"])

print ("Carrito: ", (list(productosCarrito)))

Escaneado = productosCarrito.pop()

print("Producto escaneado:", Escaneado)

print(f"Productos Restantes: {list(productosCarrito)}")










#COLAS
from collections import deque

# Inicializar la cola
cola = deque(["Cliente 1", "Cliente 2", "Cliente 3"])

# Encolar (enqueue) elementos
cola.append("Cliente 4")
print(f"Cola actual: {list(cola)}")

# Desencolar (dequeue) el primer elemento
atendido = cola.popleft()
print(f"Atendiendo a: {atendido}")

# Cola resultante
print(f"Cola después de desencolar: {list(cola)}")



#PILAS
# Inicializar la pila
pila = []

# Apilar (push) elementos
pila.append("Plato 1")
pila.append("Plato 2")
pila.append("Plato 3")

print(f"Pila actual: {pila}")

# Desapilar (pop) el último elemento
elemento_eliminado = pila.pop()
print(f"Elemento retirado: {elemento_eliminado}")

# Pila resultante
print(f"Pila después de desapilar: {pila}")

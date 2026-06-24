#6. Pilas y Colas

# Pilas (Stacks)
class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamaño(self):
        return len(self.items)

# Colas (Queues)
class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamaño(self):
        return len(self.items)
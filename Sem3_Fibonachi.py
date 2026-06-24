#10. Notacion Big O
# La notación Big O es una forma de describir la complejidad algorítmica de un algoritmo, expresando 
# cómo el tiempo de ejecución o el espacio requerido por el algoritmo crece en función del tamaño de la entrada.
# Se utiliza para clasificar algoritmos según su eficiencia, permitiendo comparar diferentes algoritmos y entender su comportamiento a medida que la entrada aumenta. Por ejemplo, un algoritmo con complejidad O(n) se considera lineal, mientras que uno con O(n^2) se considera cuadrático, indicando que el tiempo de ejecución crece más rápidamente a medida que aumenta el tamaño de la entrada.


#11. Funciones interativas y Recursivas
#11.1 Factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo

print(factorial(5))  # 120


#11.2 Fibonacci
def fibonacci(n):
    if n <= 1:  # Caso base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

print(fibonacci(6))  # 8


#11.3 Suma de una lista
def suma_lista(arr):
    if len(arr) == 0:  # Caso base
        return 0
    else:
        return arr[0] + suma_lista(arr[1:])  # Caso recursivo

print(suma_lista([1, 2, 3, 4]))  # 10


#11.4 Busqueda Binaria Recursiva
def busqueda_binaria(arr, objetivo, izq, der):
    if izq > der:  # Caso base
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:  # Caso base
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)  # Recursivo
    else:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)  # Recursivo
    


#12. Torres de Hanoi
def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:  # Caso base
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)  # Mover n-1 discos a la torre auxiliar
        print(f"Mover disco {n} de {origen} a {destino}")  # Mover el disco más grande al destino
        torres_de_hanoi(n - 1, auxiliar, destino, origen)  # Mover los n-1 discos desde la torre auxiliar al destino


#14. Funcion Finbonachi Recursiva
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


#15. Serie de fibonachi
def fibonacci_serie(n):
    serie = []
    for i in range(n):
        serie.append(fibonacci_recursivo(i))
    return serie

print(fibonacci_serie(10))  # Imprime los primeros 10 números de la serie de Fibonacci
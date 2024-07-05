
import time
import math
import matplotlib.pyplot as plt

def guerra(archivo):
    try:
        nombre_archivo = archivo + ".txt"
        with open(nombre_archivo) as archivo:
            lineas = archivo.readlines()
            batallas = []
            for linea in lineas: #O(n)
                datos = linea.strip().split(",")
                if datos[0].isnumeric() and datos[1].isnumeric():
                    tiempo = float(datos[0].strip())
                    peso = float(datos[1].strip())
                    batallas.append((tiempo, peso))
        return batallas
    except IOError:
        print("Error al abrir el archivo")
        return None

def ordenar_batallas(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: (x[0]/x[1]))
    tiempo_total = 0
    suma_ponderada = 0
    for batalla in batallas_ordenadas:
    	tiempo_total += batalla[1]  # Suma la duración de la batalla actual al tiempo total
    	suma_ponderada += tiempo_total * batalla[0] 
    	
    return batallas_ordenadas, suma_ponderada


# Realizar mediciones de tiempos
archivo = input("ingrese nombre del archivo\n")
batallas = guerra(archivo) #O(n)
n = len(batallas)
tiempos = []
for i in range(1, n+1):
    inicio = time.time()
    orden, suma_ponderada = ordenar_batallas(batallas[:i])
    fin = time.time()
    tiempos.append(fin - inicio)

# Graficar los tiempos de ejecución
escala = 10**7
tiempos_escalados = [t * escala for t in tiempos]

plt.figure(figsize=(12, 8))
plt.plot(range(1, n+1), tiempos_escalados, marker='o')
plt.plot(range(1, n+1), [i * math.log(i) for i in range(1, n+1)], 'r--', label='O(n log n)')
plt.xlabel('Número de batallas')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución del algoritmo')
plt.grid(True)
plt.show()

import os

def guerra():
    try:
        with open("batallas.txt") as archivo:
            lineas = archivo.readlines()
            batallas = []
            for linea in lineas: #O(n)
                datos = linea.strip().split(",")
                terreno = datos[0].strip()
                peso = float(datos[1].strip())
                duracion = float(datos[2].strip())
                batallas.append((terreno, peso, duracion))
        return batallas
    except IOError:
        print("Error al abrir el archivo")
        return None

def orden_1(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[1] / x[2])
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas):
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def orden_2(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[2], reverse= True)
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas):
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def orden_2_reves(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[2])
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas):
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def orden_3(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[1])
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas):
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def orden_3_reves(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[1], reverse= True)
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas):
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def orden_4(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[2] / x[1]) #O(n Log(n))
    finalizacion_tot = 0
    for i, batalla in enumerate(batallas_ordenadas): #O(n)
        terreno, peso, duracion = batalla
        finalizacion_tot += duracion
        batallas_ordenadas[i] = (terreno, peso, finalizacion_tot)
    return batallas_ordenadas

def resultado(batallas_ordenadas):
    sumatoria = 0
    print("\nEl orden de las batallas para minimizar la suma ponderada de los tiempos de finalización es:")
    for batalla in batallas_ordenadas:
        terreno , peso, duracion = batalla
        sumatoria += peso * duracion
        print(terreno)
    print("La sumatoria total es:", sumatoria)

def main():
    batallas = guerra() #O(n)
    if batallas != None:
        print("\ntest 1")
        resultado(orden_1(batallas)) #O(n Log(n))
        print("\ntest 2")
        resultado(orden_2(batallas))
        print("\ntest 2_reves")
        resultado(orden_2_reves(batallas))
        print("\ntest 3")
        resultado(orden_3(batallas))
        print("\ntest 3_reves")
        resultado(orden_3_reves(batallas))
        print("\ntest 4")
        resultado(orden_4(batallas))

main()
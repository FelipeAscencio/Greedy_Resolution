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

def resultado(batallas):
    batallas_ordenadas = sorted(batallas, key=lambda x: x[0] / x[1]) #O(n Log(n))
    finalizacion_tot = 0
    suma_ponderada = 0
    
    print("\nEl orden de las batallas para minimizar la suma ponderada de los tiempos de finalización es:")
    for batalla in batallas_ordenadas: #O(n)
        tiempo, peso = batalla
        finalizacion_tot += tiempo
        print(tiempo, peso)
        suma_ponderada += peso * finalizacion_tot
    print("La sumatoria total es:", suma_ponderada)

def main():
    archivo = input("ingrese nombre del archivo\n")
    batallas = guerra(archivo) #O(n)
    if batallas != None:
        resultado(batallas)

main()
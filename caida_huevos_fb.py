import sys
import time

sys.setrecursionlimit(1000000)
 
def caida_huevos_fb(huevos, pisos):
   
    operaciones = 0 
 
    def resolver(h, n):
        nonlocal operaciones
        if n == 0 or n == 1:
            return n
        if h == 1:
            return n
 
        minimo = sys.maxsize
        for x in range(1, n + 1):
            operaciones += 1 
 
            se_rompe = resolver(h - 1, x - 1)
            no_se_rompe = resolver(h, n - x)
 
            peor_caso = 1 + max(se_rompe, no_se_rompe)
            if peor_caso < minimo:
                minimo = peor_caso
        return minimo
 
    resultado = resolver(huevos, pisos)
    return resultado, operaciones
 
def main():
    print("=" * 60)
    print("  CAIDA DE HUEVOS - FUERZA BRUTA (RECURSION)  ")
    print("=" * 60)
    try:
        huevos = int(input("Ingrese la cantidad de huevos: "))
        pisos = int(input("Ingrese la cantidad de pisos: "))
    except ValueError:
        print("Entrada invalida. Debe ingresar numeros enteros.")
        return
 
    if huevos < 1 or pisos < 0:
        print("Los huevos deben ser >= 1 y los pisos >= 0.")
        return
 
    inicio = time.perf_counter()
    resultado, operaciones = caida_huevos_fb(huevos, pisos)
    fin = time.perf_counter()
 
    memoria_auxiliar = huevos + pisos
 
    print("-" * 60)
    print(f"Con {huevos} huevo(s) y {pisos} piso(s):")
    print(f"Minimo de lanzamientos en el peor caso = {resultado}")
    print(f"Cantidad de operaciones = {operaciones}")
    print(f"Memoria auxiliar (pila de recursion) = {memoria_auxiliar} niveles")
    print(f"Tiempo de ejecucion = {(fin - inicio) * 1000:.4f} ms")
    print("=" * 60)
 
if __name__ == "__main__":
    main()
import sys
import time

def caida_huevos_pd(huevos, pisos):
    dp = [[0] * (pisos + 1) for _ in range(huevos + 1)]
    memoria_celdas = (huevos + 1) * (pisos + 1)
    operaciones = 0
 
    for n in range(1, pisos + 1):
        dp[1][n] = n

    for k in range(1, huevos + 1):
        if pisos >= 1:
            dp[k][1] = 1
 
    for k in range(2, huevos + 1):
        for n in range(2, pisos + 1):
            mejor = sys.maxsize
            for x in range(1, n + 1):
                operaciones += 1 
                peor = 1 + max(dp[k - 1][x - 1], dp[k][n - x])
                if peor < mejor:
                    mejor = peor
            dp[k][n] = mejor
 
    return dp[huevos][pisos], operaciones, memoria_celdas, dp
 
def primer_piso_optimo(huevos, pisos, dp):
    if pisos == 0 or pisos == 1 or huevos == 1:
        return 1 if pisos >= 1 else 0
    objetivo = dp[huevos][pisos]
    for x in range(1, pisos + 1):
        peor = 1 + max(dp[huevos - 1][x - 1], dp[huevos][pisos - x])
        if peor == objetivo:
            return x
    return 1
 
def main():
    print("=" * 60)
    print("  CAIDA DE HUEVOS - PROGRAMACION DINAMICA (TABULACION)  ")
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
    resultado, operaciones, memoria_celdas, dp = caida_huevos_pd(huevos, pisos)
    fin = time.perf_counter()
 
    piso = primer_piso_optimo(huevos, pisos, dp)
 
    print("-" * 60)
    print(f"Con {huevos} huevo(s) y {pisos} piso(s):")
    print(f"Minimo de lanzamientos en el peor caso = {resultado}")
    print(f"Primer lanzamiento optimo desde el piso = {piso}")
    print(f"Cantidad de operaciones = {operaciones}")
    print(f"Memoria usada (celdas de la tabla dp) = {memoria_celdas}")
    print(f"Tiempo de ejecucion = {(fin - inicio) * 1000:.4f} ms")
    print("=" * 60)
 
if __name__ == "__main__":
    main()
 
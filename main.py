# M1. Actividad
# Juan Daniel Rodríguez Oropeza A01411625
import time

from cleaning_model import CleaningModel

# Dimensiones del espacio
M = int(input("Introduce el valor de M: ")) # alto
N = int(input("Introduce el valor de N: ")) # ancho

CANT_AGENTES = int(input("Introduce la cantidad de agentes: ")) # Cantidad de agentes

PORCENTAJE_SUCIAS = float(input("Introduce el porcentaje inicial de celdas sucias: ")) # Porcentaje de celdas que inicialmente están sucias
while (PORCENTAJE_SUCIAS > 1):
    print("Los valores de porcentaje van de 0 a 1. Intenta de nuevo.")
    PORCENTAJE_SUCIAS = float(input("Introduce el porcentaje inicial de celdas sucias: "))

TIEMPO_MAX = int(input("Introduce el tiempo máximo de ejecución (segundos): ")) # Tiempo máximo de ejecución del algoritmo

def basic_example():
    model = CleaningModel(CANT_AGENTES, N, M, PORCENTAJE_SUCIAS, TIEMPO_MAX)
    while (model.celdas_suc > 0 and ((time.time() - model.init_time) < model.final_time)):
        model.step()
        [print(*line) for line in model.dirty_matrix]
        print("\nPorcentaje de celdas limpias:", model.porcentaje_celdas_limpias())
        print("\n=================================================\n")

    print("Cantidad total de movimientos por todos los agentes:", model.total_movimientos())
    print("Tiempo total:", model.final_time)

basic_example()
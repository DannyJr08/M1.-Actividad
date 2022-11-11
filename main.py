import cleaning_model as CleaningModel
import matplotlib.pyplot as plt

# Dimensiones del espacio
M = 10
N = 10

CANT_AGENTES = 3 # Cantidad de agentes

P_SUCIAS = 0.6 # Porcentaje de celdas que regularmente están sucias

TIEMPO_MAX = 2 # Tiempo máximo de ejecución del algoritmo

# Nivel de carga máximo de los agentes. Puede ser en porcentaje o en unidades de carga
CARGA_MAX = 100

def basic_example():
    # empty_model = MoneyModel(10)
    # empty_model.step()

    model = CleaningModel(10)
    for i in range(10):
        model.step()
        print("\n")

    agent_counter = [a.counter for a in model.schedule.agents]
    print(agent_counter)

    plt.hist(agent_counter)
    plt.show()
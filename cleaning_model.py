import mesa
import random
import numpy as np
import pandas as pd

class CleaningAgent(mesa.Agent):
    # Se inicializa un agente.
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.counter = 0 # Contador de pasos

    def step(self):
        self.move()
        self.clean()

    # Función que hace que se mueva el agente
    def move(self):
        # El agente primeramente checa su alrededor para
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.counter = self.counter + 1

    def clean(self):
        if not self.model.estaLimpio(self.pos):
            self.model.cambiarLimpiar(self.pos)
            #print(agente)
        pass


class CleaningModel(mesa.Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height, percent):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.init_time = None
        self.final_time = None

        # Inicializar matriz aleatoriamente
        self.celdas_suc = (width * height) + percent
        self.celdas_lim = (width * height) * (1 - percent)
        self.dirty_matrix = None

        # Create agents
        for i in range(self.num_agents):
            a = CleaningAgent(i, self)
            self.schedule.add(a)

            # Add the agent to a random grid cell
            # x = self.random.randrange(self.grid.width)
            # y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (1, 1))

    def step(self):
        # Advance the model by one step.
        self.schedule.step()

    def estaLimpio(self, new_position):
        x, y = new_position
        pass

    def cambiarLimpio(self, new_position):
        # establecemos a verdadero el valor de la matriz en esa posición
        self.celdas_suc = self.celdas_suc - 1
        self.celdas_lim = self.celdas_lim + 1
        if self.celdas_suc == 0:
            self.final_time = 5
'''
def inicializarEspacio(modelo):
    grid = np.zeros((modelo.grid.width, modelo.grid.height))
    for celda in modelo.grid.coord_iter():
        contenidoCelda, x, y = celda
        for objeto in contenidoCelda:
            if isinstance(objeto, CleaningAgent):
                grid[x][y] = 2
            elif isinstance(objeto, Celda):
                grid[x][y] = objeto.state
    return grid
'''
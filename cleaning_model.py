import mesa
import time
import random

class CleaningAgent(mesa.Agent):
    # Se inicializa un agente.
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    # Función que ejecuta el agente al moverse
    def step(self):
        self.move() # Cambia de posición
        self.clean() # Limpia la celda si está sucia

    # Función que hace que se mueva el agente
    def move(self):
        # El agente primeramente checa su alrededor para saber a donde moverse
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps) # El agente escoge una posición
        self.model.grid.move_agent(self, new_position) # El agente se coloca en su nueva posición.
        #print("Yo:", self.unique_id, " me he movido a la casilla", new_position)

    # Función que hace que el agente limpie la casilla en caso de que esté sucia
    def clean(self):
        # Si está sucia la casilla en la que se encuentra el agente limpiador, la limpia
        if not self.model.estaLimpio(self.pos):
            self.model.cambiarLimpio(self.pos)
            print("Limpié la celda: ", self.pos, "\n")


class CleaningModel(mesa.Model):
    # A model with some number of agents.
    def __init__(self, N, width, height, percent, tiempo_max):
        self.num_agents = N
        #print("Numero de agentes:", self.num_agents)
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(height, width, True)
        self.init_time = time.time()
        self.final_time = tiempo_max
        self.total_mov = 0

        # Inicializar matriz aleatoriamente
        self.celdas_suc = int((width * height) * percent)
        self.celdas_lim = int((width * height) * (1 - percent))
        self.dirty_matrix = [([True]*width) for i in range(height)] # Al principio todas las celdas se inicializan como Verdadero, es decir, que están limpias
        self.cant_celdas_suc_inicializar = self.celdas_suc
        #print("celda suc", self.cant_celdas_suc_inicializar)
        while (self.cant_celdas_suc_inicializar > 0): # Cuando ya no queden celdas por inicializar a sucias (False)
            # Se recorren todas las celdas de la matriz.
            for i in range(height):
                for j in range(width):
                    sucio_o_limpio = random.randint(0, 1) # Se decide aleatoriamente si la celda actual permancerá limpia o se cambiará a sucia
                    if self.cant_celdas_suc_inicializar > 0 and self.dirty_matrix[i][j]: # Si la celda se decide que será sucia y la celda está limpia, y además, aún quedan celdas por inciializar a sucias...
                        self.dirty_matrix[i][j] = False # La celda se
                        self.cant_celdas_suc_inicializar -= 1
                        #print("Celda cambiada", i, j ,"a", self.dirty_matrix[i][j])
                        #print("Ahora quedan por cambiar", self.cant_celdas_suc_inicializar)
            #print("cant celdas suc", self.cant_celdas_suc_inicializar)

        # Create agents
        for i in range(self.num_agents):
            a = CleaningAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (1, 1))

    def step(self):
        # Advance the model by one step.
        self.total_mov += 1
        self.schedule.step()

    def estaLimpio(self, new_position):
        x, y = new_position
        return self.dirty_matrix[x][y]

    def cambiarLimpio(self, new_position):
        # Establecemos a verdadero el valor de la matriz en esa posición
        x, y = new_position
        self.dirty_matrix[x][y] = True
        self.celdas_suc -= 1
        self.celdas_lim += 1
        # Si ya están todas las celdas limpias...
        if self.celdas_suc == 0:
            self.final_time = time.time() - self.init_time # Se calcula el tiempo que duró la ejecución del programa
            self.total_movimientos() # Se calcula el total de movimientos por todos los agentes

    def total_movimientos(self):
        return self.total_mov * self.num_agents

    def porcentaje_celdas_limpias(self):
        return self.celdas_lim / (self.celdas_lim + self.celdas_suc)
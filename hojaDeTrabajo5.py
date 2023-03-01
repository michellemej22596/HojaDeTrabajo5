# 28/02/2023
# Michelle Mejía 22596
# Simulador Simpy

import random
import simpy

env = simpy.Environment()
averageTime = 0

# Variables para determinar efectividad
processes= 25 #25, 50, 100, 150, 200
interval = 10.0 #10, 5, 1
RAM = simpy.Container(env, init=100, capacity=100) #init 200
instructions= 3 #3 o 6 por unidad de tiempo
processors = 1 #1 o 2



#random.seed(RANDOM_SEED)
#timeToWait= random.expovariate(1.0 / interval)
# RAM.get(memory) memory es el parámetro que tiene el número de memoria a utilizar RAM.put(memoria)


class Simulation:

    def new(self):
        pass
    def ready(self):
        pass
    def waiting(self):
        pass
    def running(self):
        pass
    def terminated(self):
        pass
    def randomGenerator():
        pass

sim = Simulation()

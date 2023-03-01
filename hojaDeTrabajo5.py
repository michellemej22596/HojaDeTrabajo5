# 28/02/2023
# Michelle Mejía 22596
# Simulador Simpy

import random
import simpy

env = simpy.Environment()
processes= 200 #25, 50, 100, 150, 200
interval = 1.0 #10, 5, 1
RAM = simpy.Container(env, init=100, capacity=100) #init and capacity 200
CPU = simpy.Resource(env, capacity=1) 	  
processors = 1 #1 o 2
random.seed(10)


def source(env, processes, RAM, interval, CPU):
    #Generating processes
    for i in range(processes):
        p = process(env, 'Process%02d' % i, RAM, CPU, time_in_bank=12.0)
        env.process(p)
        timeToWait= random.expovariate(1.0 / interval)
        print("Un proceso se ha generado, con un tiempo de espera de", round(timeToWait, 2))
        yield env.timeout(timeToWait)

def process(env, name, RAM, CPU, time_in_bank):
    #Llegada del proceso
    arrive = env.now
    RAM.get(10)
    if RAM.level>0:
        print('%7.4f %s: Un proceso ha llegado' % (arrive, name))
    else: 
        print("La RAM se encuentra llena, por favor espere a que se desocupe")
        yield env.timeout(5)

    with CPU.request() as req:
        instructions = random.uniform(1, 10)
        # Wait for the CPU or abort at the end of our tether
        results = yield req | env.timeout(instructions)

        wait = env.now - arrive

        if req in results:
            # We got to the CPU
            print('%7.4f %s: El proceso ha esperado %6.3f' % (env.now, name, wait))

            tib = random.expovariate(1.0 / time_in_bank)
            yield env.timeout(tib)
            print('%7.4f %s: El proceso ha sido terminado' % (env.now, name))
            RAM.put(10)

        else:
            # cola
            print('%7.4f %s: El proceso a permanecido en cola por %6.3f' % (env.now, name, wait))

print("Bienvenido a la simulación")
env.process(source(env, processes, RAM, interval, CPU))
env.run()
print("Simulation complete")

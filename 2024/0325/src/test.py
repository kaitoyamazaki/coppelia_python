from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import pandas as pd
from time import sleep

class Simulation:

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        self.obj1 =  sim.getObject("/object1")
        self.obj2 = sim.getObject("/object2")

        self.moving_value = 0.0005



    def simulation(self):

        sim = self.sim
        sim.startSimulation()

        while sim.getSimulationTime() < 100:
            obj1 = sim.getObjectPosition(self.obj1, sim.handle_world)
            obj2 = sim.getObjectPosition(self.obj2, sim.handle_world)

            obj1[0] = obj1[0] - self.moving_value
            obj2[0] = obj2[0] + self.moving_value

            sim.setObjectPosition(self.obj1, obj1, sim.handle_world)
            sim.setObjectPosition(self.obj2, obj2, sim.handle_world)

            self.check_collision()



        sim.stopSimulation()
    
    def check_collision(self):
        sim = self.sim

        result, handles = sim.checkCollision(self.obj1, self.obj2)

        if result == 1:
            print(f"衝突しています")

def main():

    try:
        simulation = Simulation()
        simulation.simulation()
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")
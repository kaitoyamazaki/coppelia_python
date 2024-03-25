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

    def simulation(self):

        sim = self.sim
        sim.startSimulation()

        while sim.getSimulationTime() < 50:
            obj1 = sim.getObjectPosition(self.obj1, sim.handle_world)
            obj2 = sim.getObjectPosition(self.obj2, sim.handle_world)

            obj1[0] = obj1[0] - 0.05
            obj2[0] = obj2[0] + 0.05

            print(f"obj1:{obj1}, obj2:{obj2}")


        sim.stopSimulation()

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
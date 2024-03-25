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
            print(f"test")

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
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Simulation:

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
    
    def simulation(self):
        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        while (t := sim.getSimulationTime()) < 3:
            print(f"Simulation time: {t: .2f} [s]")
            sim.step()
        sim.stopSimulation()


    
def main():
    simulator = Simulation()
    simulator.simulation()
    

if __name__ == '__main__':
    
    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Threelink():
    
    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim
        self.base = sim.getObject("/base")
        self.link1 = sim.getObject("/base/ForceSensor/link1")
        self.j1 = sim.getObject("/base/ForceSensor/link1/joint")
        self.link2 = sim.getObject("/base/ForceSensor/link1/joint/link2")
        self.j2 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3")
        self.j3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint")
        self.link4 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4")
        self.p_e = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4/p_e")

        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2
    

    def simulation(self):
        sim = self.sim






def main():
    simulator = Threelink()
    simulator.simulation()


if __name__ == "__main__":
    main()
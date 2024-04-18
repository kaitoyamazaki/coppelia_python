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

        self.object = sim.getObject("/target_object")
        self.object_cog = sim.getObject("/target_object/cog")

        self.right_hand = sim.getObject("/BaseRobot/right_hand")
        self.left_hand = sim.getObject("/BaseRobot/left_hand")

        self.contact_point1 = sim.getObject('/target_object/contact_point1')
        self.contact_point2 = sim.getObject('/target_object/contact_point2')
        self.contact_point3 = sim.getObject('/target_object/contact_point3')
    
    def check_parameter(self, sim):

        pos_of_contact_point1 = sim.getObjectPosition(self.contact_point1, sim.handle_world)
        pos_of_contact_point2 = sim.getObjectPosition(self.contact_point2, sim.handle_world)
        pos_of_contact_point3 = sim.getObjectPosition(self.contact_point3, sim.handle_world)

        pos_of_cog = sim.getObjectPosition(self.cog, sim.handle_world)



def main():

    try:
        simulation = Simulation()
        simulation.check_parameter(simulation.sim)
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")
# 対象物体をTypeBの状態でその場回転させるプログラム
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
from time import sleep

class Simulation:

    def __init__(self):
        
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        self.j1 = sim.getObject("/BaseRobot/j1")
        self.j2 = sim.getObject("/BaseRobot/j2")
        self.j3 = sim.getObject("/BaseRobot/j3")
        self.j4 = sim.getObject("/BaseRobot/j4")
        self.j5 = sim.getObject("/BaseRobot/j5")
        self.j6 = sim.getObject("/BaseRobot/j6")
        self.coe = sim.getObject("/BaseRobot/CoP")

        self.tip = sim.getObject("/target")

        self.robot = sim.getObject("/BaseRobot")

        self.l1 = 0.13156
        self.l2 = 0.1104
        self.l3 = 0.096
        self.l4 = 0.07318
        
    # シミュレーションに反映する関数
    def simulation(self):
        
        sim = self.sim
        #data = self.data

        #sim.setStepping(True)
        sim.startSimulation()

        while sim.getSimulationTime() < 100:

            theta1 = sim.getJointPosition(self.j1)
            z_new_theta = self.calc_j2(sim, theta1)

            sim.setJointPosition(self.j1, z_new_theta)

        #sleep(5)

        sim.stopSimulation()
    

    def calc_j2(self, sim, theta):

        theta = np.rad2deg(theta)
        if (theta < 0.0 and theta > -0.05):
            pass

        else:
            theta = theta + 0.05

        #print(f'theta : {theta}')
        theta = np.deg2rad(theta)

        return theta


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
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

from myclass.velocity_IK_xy import *
from myclass.velocity_IK_xz import *

class Simulation():

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        # モデルの情報を取得
        self.base = sim.getObject("/base")
        self.joint1 = sim.getObject("/base/joint")
        self.link1 = sim.getObject("/base/joint/link1")
        self.joint2 = sim.getObject("/base/joint/link1/joint")
        self.link2 = sim.getObject("/base/joint/link1/joint/link2")
        self.joint3 = sim.getObject("/base/joint/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/joint/link1/joint/link2/joint/link3")
        self.joint4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint")
        self.link4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4")
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4/p_e")
        self.p_t = sim.getObject("/p_t")

        self.pt_x = 1.1
        self.pt_y = 0.4
        self.pt_z = 0.4
        self.pt_theta = 0.0
        self.target_xy_theta = np.arctan2(self.pt_y, self.pt_x)

    
    def simulation(self):

        sim = self.sim
        sim.setStepping(True)
        sim.startSimulation()

        pos_of_pt = self.assign_pt()

        sim.setObjectPosition(self.p_t, [pos_of_pt[0], pos_of_pt[1], pos_of_pt[2]], sim.handle_world)
        sim.setObjectOrientation(self.p_t, [0.0, pos_of_pt[3], 0], sim.handle_world)

        #sim.setJointPosition(self.joint1, j1_theta)

        while (t := sim.getSimulationTime()) < 100:

            IK_xy = IK_XY(self.sim)
            j1_theta = IK_xy.IK()

            #yakobi = IK_xz.IK()

            sim.setJointPosition(self.joint1, j1_theta)
            sim.step()
        
        sim.stopSimulation()

    
    def assign_pt(self):

        pos_of_pt = np.empty(4)

        pos_of_pt[0] = self.pt_x
        pos_of_pt[1] = self.pt_y
        pos_of_pt[2] = self.pt_z
        pos_of_pt[3] = self.pt_theta

        return pos_of_pt


def main():

    simulation = Simulation()
    simulation.simulation()
    #IK_xz = IK_XZ() 



if __name__ == "__main__":
    main()
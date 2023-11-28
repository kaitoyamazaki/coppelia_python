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

        sim.setStepping(True)
        sim.startSimulation()

        i = 0.5

        while (t := sim.getSimulationTime()) < 7:
            #print(f"Simulation time: {t: .2f} [s]")
            self.move_arm(i)
            sim.step()
            i = i + 0.0005
        
        sim.stopSimulation()

    def move_arm(self, x):
        sim = self.sim
        l1 = self.l1
        l2 = self.l2
        l3 = self.l3
        l4 = self.l4

        j1 = self.j1
        j2 = self.j2
        j3 = self.j3

        xe = x
        ye = 0
        theta_e = np.deg2rad(-90)

        p3_x = xe - 0.2
        p3_y = 0

        l5 = p3_x

        #j1の角度を求める
        c1 = (l2 * l2 + l5 * l5 - l3 * l3) / (2 * l2 * l5)
        #print(f"c1 is {c1}")
        j1_rad = np.arccos(c1)
        j1_rad = j1_rad - (np.pi / 2)

        #j2の角度を求める
        c2 = (l2 * l2 + l3 * l3 - l5 * l5) / (2 * l2 * l3)
        #print(f"c2 is {c2}")
        beta = np.arccos(c2)
        j2_rad = np.pi - beta
        j2_rad = -j2_rad

        #j3の角度を求める

        j3_motor = theta_e -j1_rad -j2_rad

        joint = np.empty(3)

        joint[0] = j1_rad
        joint[1] = j2_rad
        joint[2] = j3_motor

        #joint_deg = np.rad2deg(joint)

        #print(f"{joint_deg}")

        sim.setJointPosition(j1, j1_rad)
        sim.setJointPosition(j2, j2_rad)
        sim.setJointPosition(j3, j3_motor)


def main():
    simulator = Threelink()
    simulator.simulation()


if __name__ == "__main__":
    main()
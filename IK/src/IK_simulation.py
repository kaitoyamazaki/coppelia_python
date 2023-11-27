from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import time

class Simulation:

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim
        self.base = sim.getObject("/base")
        self.joint1 = sim.getObject("/base/joint")
        self.link1 = sim.getObject("/base/joint/link1")
        self.joint2 = sim.getObject("/base/joint/link1/joint")
        self.link2 = sim.getObject("/base/joint/link1/joint/link2")

        self.first_deg_joint1 = sim.getJointPosition(self.joint1)
        self.first_deg_joint2= sim.getJointPosition(self.joint2)
        self.l1 = 1
        self.l2 = 0.5

    
    def simulation(self):
        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        target_x, target_y = self.input_target()
        dq = self.get_div_pos(target_x, target_y)

        result = self.IK(self.first_deg_joint1, self.first_deg_joint2, dq)

        sim.setJointPosition(self.joint1, result[0][0])
        sim.setJointPosition(self.joint2, result[1][0])

        while (t := sim.getSimulationTime()) < 20:
            #pos = sim.getJointPosition(self.joint2)
            #print(f"Simulation time: {t: .2f} [s]")
            sim.setJointPosition(self.joint1, result[0][0])
            sim.setJointPosition(self.joint2, result[1][0])
            sim.step()
        
        sim.stopSimulation()
    
    def get_div_pos(self, x, y):
        l1 = self.l1
        l2 = self.l2

        first_x = l1 * np.cos(0) + l2 * np.cos(np.deg2rad(0+90))
        first_y = l1 * np.sin(0) + l2 * np.sin(np.deg2rad(0+90))

        dx = x - first_x
        dy = y - first_y

        dq = np.empty((2,1))
        dq[0][0] = dx
        dq[1][0] = dy

        print(f"{dq}")

        return dq


    def input_target(self):

        x = 1.2
        y = -0.3
        #x, y = map(float, input("Enter x, y of the Endeffector : ").split(','))

        return x, y

    def IK(self, j1, j2, dq):
        l1 = self.l1
        l2 = self.l2

        now_rad = self.get_now_joint()

        first_IK = self.calc_IK(l1, l2, j1, j2)

        result = np.dot(first_IK, dq)

        result = now_rad + result

        print(f"result is {np.rad2deg(result)}")

        return result



    
    def get_now_joint(self):
        now_joint = np.empty((2,1))
        now_joint[0][0] = self.first_deg_joint1
        now_joint[1][0] = self.first_deg_joint2

        print(f"{now_joint}")

        return now_joint




    
    def calc_IK(self, l1, l2, j1, j2):
        IK_queue = np.empty((2,2))
        IK_queue[0][0] = (l2 * np.cos(j1 + j2)) / (l1 * l2 * np.sin(j2))
        IK_queue[0][1] = (l2 * np.sin(j1 + j2)) / (l1 * l2 * np.sin(j2))
        IK_queue[1][0] = (-l1 * np.cos(j1) - l2 * np.cos(j1 + j2)) / (l1 * l2 * np.sin(j2))
        IK_queue[1][1] = (-l1 * np.sin(j1) - l2 * np.sin(j1 + j2)) / l1 * l2 * np.sin(j2)

        return IK_queue

    
def main():
    simulator = Simulation()
    simulator.simulation()
    

if __name__ == '__main__':
    
    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
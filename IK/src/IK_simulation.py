from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

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
        dx, dy = self.get_div_pos(target_x, target_y)

        print(f"dx, dy is {dx, dy}")

        #result_j1, result_j2 = self.IK(self.first_deg_joint1, self.first_deg_joint2, dx, dy)

        while (t := sim.getSimulationTime()) < 3:
            #pos = sim.getJointPosition(self.joint2)
            print(f"Simulation time: {t: .2f} [s]")
            sim.step()
        sim.stopSimulation()
    
    def get_div_pos(self, x, y):
        l1 = self.l1
        l2 = self.l2

        first_x = l1 * np.cos(0) + l2 * np.cos(np.deg2rad(0+90))
        first_y = l1 * np.sin(0) + l2 * np.sin(np.deg2rad(0+90))

        dx = x - first_x
        dy = y - first_y

        return dx, dy


    def input_target(self):

        x = 1.2
        y = -0.3
        #x, y = map(float, input("Enter x, y of the Endeffector : ").split(','))

        return x, y

    def IK(self, j1, j2, x, y):
        l1 = self.l1
        l2 = self.l2

        first_IK = self.calc_IK(l1, l2, j1, j2)




    
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
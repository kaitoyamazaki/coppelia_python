from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Simulation:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        self.base = sim.getObject("/base")
        self.link1 = sim.getObject("/base/ForceSensor/link1")
        self.joint1 = sim.getObject("/base/ForceSensor/link1/joint")
        self.link2 = sim.getObject("/base/ForceSensor/link1/joint/link2")
        self.joint2 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3")
        self.joint3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint")
        self.link4 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4")
        self.p_e = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4/p_e")

        self.target_pos_x = 1.3
        self.target_pos_y = 0.4
        self.dp = 0.001

        #self.p_target = sim.getObject("/p_target")
        self.first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)

        self.first_deg_joint1 = sim.getJointPosition(self.joint1)
        self.first_deg_joint2= sim.getJointPosition(self.joint2)
        self.first_deg_joint3= sim.getJointPosition(self.joint3)
        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2 

    def simulation(self):
        
        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        # 最終的な目標値の入力を行う
        target_pos = self.input_target_pos()

        #print(f"最初の角度を取りえず出力する : {self.first_deg_joint1}, {self.first_deg_joint2}, {self.first_deg_joint3}")
    
        while (t := sim.getSimulationTime()) < 100:

            sim.step()
        
        sim.stopSimulation()

    def input_target_pos():
    
        target_pos = np.empty((1,2))

        target_pos[0][0] = self.target_pos_x
        target_pos[0][1] = self.target_pos_y

        return target_pos



def main():
    simulation = Simulation()
    simulation.simulation()


if __name__ == '__main__':
    main()
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Yakobi3link():
    
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

        self.first_rad_joint1 = sim.getJointPosition(self.j1)
        self.first_rad_joint2 = sim.getJointPosition(self.j2)
        self.first_rad_joint3 = sim.getJointPosition(self.j3)
        self.first_joint = np.empty((3,1))

        self.first_joint[0][0] = self.first_rad_joint1
        self.first_joint[1][0] = self.first_rad_joint2
        self.first_joint[2][0] = self.first_rad_joint3
    

    def simulation(self):
        sim = self.sim



        first_yakobi, first_inv_yakobi = self.get_first_yakobi()

        print(f"first inv yakobi is {first_inv_yakobi}")
        dq = self.get_dq()

        print(f"dq is {dq}")
        #j1, j2, j3 = self.test_inv_yakobi()

        result = np.dot(first_inv_yakobi, dq)
        print(f"first_joint is {self.first_joint}")
        result = self.first_joint + result

        print(f"result is {result}")

        sim.setStepping(True)
        sim.startSimulation()

        i = 0.5

        while (t := sim.getSimulationTime()) < 7:
            #print(f"Simulation time: {t: .2f} [s]")
            #self.move_arm_yakobi(i)
            sim.setJointPosition(self.j1, result[0][0])
            sim.setJointPosition(self.j2, result[1][0])
            sim.setJointPosition(self.j3, result[2][0])

            if (t == 0):
                print(f"unko")

            sim.step()
            i = i + 0.0005
        
        sim.stopSimulation()

    
    def get_dq(self):
        sim = self.sim
        pos_e = sim.getObjectPosition(self.p_e, sim.handle_world)
        target_x = 0.1
        target_z = 1.55
        target_theta = np.deg2rad(0)
        dq = np.empty((3,1))

        dx = target_x - pos_e[0]
        dz = target_z - pos_e[2]
        dtheta = target_theta - self.first_rad_joint1

        dq[0][0] = dx
        dq[1][0] = dz
        dq[2][0] = dtheta

        return dq


    def move_arm_yakobi(self, x):
        pass
    
    def get_first_yakobi(self):
        yakobi = np.empty((3,3))
        l2 = self.l2
        l3 = self.l3
        l4 = self.l4

        pi = np.pi
        half_pi = pi / 2

        j1_rad = self.first_rad_joint1
        j2_rad = self.first_rad_joint2
        j3_rad = self.first_rad_joint3

        yakobi[0][0] = -l2 * np.sin(j1_rad) - l3 * np.sin(j1_rad + j2_rad) - l4 * np.sin(j1_rad + j2_rad + j3_rad)
        yakobi[0][1] = -l3 * np.sin(j2_rad + j3_rad) - l4 * np.sin(j1_rad + j2_rad + j3_rad)
        yakobi[0][2] = -l3 * np.sin(j1_rad + j2_rad + j3_rad)

        yakobi[1][0] = l2 * np.cos(j1_rad) + l3 * np.cos(j1_rad + j2_rad) + l4 * np.cos(j1_rad + j2_rad + j3_rad)
        yakobi[1][1] = l3 * np.cos(j1_rad + j2_rad) + l4 * np.cos(j1_rad + j2_rad + j3_rad)
        yakobi[1][2] = l3 * np.cos(j1_rad + j2_rad + j3_rad)

        yakobi[2][0] = 1
        yakobi[2][1] = 1
        yakobi[2][2] = 1

        inv_yakobi = np.linalg.inv(yakobi)
        print(f"tasikame is {np.dot(yakobi, inv_yakobi)}")


        return yakobi, inv_yakobi



def main():
    simulator = Yakobi3link()
    simulator.simulation()


if __name__ == "__main__":
    main()
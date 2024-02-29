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
        
    def simulation(self):
        
        sim = self.sim
        #data = self.data

        #sim.setStepping(True)
        sim.startSimulation()

        while sim.getSimulationTime() < 200:

            theta1 = sim.getJointPosition(self.j1)
            theta2 = sim.getJointPosition(self.j2)
            theta3 = sim.getJointPosition(self.j3)
            theta4 = sim.getJointPosition(self.j4)
            theta5 = sim.getJointPosition(self.j5)
            theta6 = sim.getJointPosition(self.j6)

            yakobi = self.calc_yakobi_row(theta1, theta2, theta3, theta4)
            yakobi_inv = np.linalg.inv(yakobi)
            
            theta = np.empty((1,4))
            theta[0][0] = theta1
            theta[0][1] = theta2
            theta[0][2] = theta3
            theta[0][3] = theta4
            theta = theta.T
            theta_deg = np.rad2deg(theta)

            dp = self.calc_dp2()

            dtheta = np.dot(yakobi_inv, dp)
            dtheta_T = dtheta.T

            new_theta = theta + np.dot(yakobi_inv, dp)

            z_theta = self.calc_z_theta(theta6)
            z_new_theta = theta6 + z_theta

            #print(f"新しい new theta(予定) : {z_new_theta}")

            sim.setJointPosition(self.j1, new_theta[0][0])
            sim.setJointPosition(self.j2, new_theta[1][0])
            sim.setJointPosition(self.j3, new_theta[2][0])
            sim.setJointPosition(self.j4, new_theta[3][0])
            sim.setJointPosition(self.j6, z_new_theta)

            # 今後必要となる角度を出力するprint
            #print(f"{new_theta_deg[0][0]}, {new_theta_deg[1][0]-90}, {new_theta_deg[2][0]}, {new_theta_deg[3][0]}")

            #for i in range(len(data)): #for文らしいです

            #theta1 = sim.getJointPosition(self.j1)
            #theta2 = sim.getJointPosition(self.j2)
            #theta3 = sim.getJointPosition(self.j3)
            #theta4 = sim.getJointPosition(self.j4)

            #yakobi = self.calc_yakobi_row(theta1, theta2, theta3, theta4)

            ##print(f"yakobi : {yakobi}")
            #yakobi_inv = np.linalg.inv(yakobi)
            ##print(f"yakobi_inv : {yakobi_inv}")

            #theta = np.empty((1,4))
            #theta[0][0] = theta1
            #theta[0][1] = theta2
            #theta[0][2] = theta3
            #theta[0][3] = theta4
            #theta = theta.T
            #theta_deg = np.rad2deg(theta)

            ##print(f"{theta}")
            ##print(f"{theta_deg[0][0]}, {theta_deg[1][0]}, {theta_deg[2][0]}, {theta_deg[3][0]}")

            #dp = self.calc_dp(data[i])

            ##print(f"{dp.T}")

            #dtheta = np.dot(yakobi_inv, dp)
            #dtheta_T = dtheta.T
            ##print(f"{dtheta_T[0][0]}, {dtheta_T[0][1]}, {dtheta_T[0][2]}, {dtheta_T[0][3]}")
            #new_theta = theta + np.dot(yakobi_inv, dp)
            #new_theta_deg = np.rad2deg(new_theta)

            #sim.setJointPosition(self.j1, new_theta[0][0])
            #sim.setJointPosition(self.j2, new_theta[1][0])
            #sim.setJointPosition(self.j3, new_theta[2][0])
            #sim.setJointPosition(self.j4, new_theta[3][0])


            ##print(f"{theta2}, {theta3}, {theta4}")
            ##print(f"{yakobi}")
            ##print(f"{yakobi_inv}")
            ##print(f"{dp}")
            #print(f"{new_theta_deg[0][0]}, {new_theta_deg[1][0]-90}, {new_theta_deg[2][0]}, {new_theta_deg[3][0]}")


            #sim.step()
            #time.sleep(0.1) # for文の終わりらしいです
        
        sim.stopSimulation()
    
    def calc_yakobi_row(self, j1, j2, j3, j4):

        l1 = self.l1
        l2 = self.l2
        l3 = self.l3
        l4 = self.l4

        yakobi = np.empty((4,4))

        yakobi[0][0] = -np.cos(j1) * (l2 * np.cos(j2) + l3 * np.cos(j2+j3) + l4 * np.cos(j2+j3+j4))
        yakobi[0][1] = np.sin(j1) * (l2 * np.sin(j2) + l3 * np.sin(j2+j3) + np.sin(j2+j3+j4))
        yakobi[0][2] = np.sin(j1) * (l3 * np.sin(j2+j3) + l4 * np.sin(j2+j3+j4))
        yakobi[0][3] = l4 * np.sin(j1) * np.sin(j2+j3+j4)

        yakobi[1][0] = -np.sin(j1) *(l2 * np.cos(j2) + l3 * np.cos(j2+j3) + l4 * np.cos(j2+j3+j4))
        yakobi[1][1] = -np.cos(j1) * (l2 * np.sin(j2) + l3 * np.sin(j2+j3) + l4 * np.sin(j2+j3+j4))
        yakobi[1][2] = -np.cos(j1) * (l3 * np.sin(j2+j3) + l4 * np.sin(j2+j3+j4))
        yakobi[1][3] = -l4 * np.cos(j1) * np.sin(j2+j3+j4)

        yakobi[2][0] = 0
        yakobi[2][1] = l2 * np.cos(j2) + l3 * np.cos(j2+j3) + l4 * np.cos(j2+j3+j4)
        yakobi[2][2] = l3 * np.cos(j2+j3) + l4 * np.cos(j2+j3+j4)
        yakobi[2][3] = l4 * np.cos(j2+j3+j4)
        
        yakobi[3][0] = 0
        yakobi[3][1] = 1
        yakobi[3][2] = 1
        yakobi[3][3] = 1

        return yakobi

    
    def calc_dp(self, data):

        sim = self.sim

        #print(f"{data}")
        pos = sim.getObjectPosition(self.coe, sim.handle_world)
        #print(f"{data[3]}, {data[4]}")
        x_dp = data[3] - pos[0]
        y_dp = data[4] - pos[1] 
        z_dp = 0.0
        theta_dp = 0.0
        dp = np.empty((4,1))

        dp[0][0] = x_dp
        dp[1][0] = y_dp
        dp[2][0] = z_dp
        dp[3][0] = theta_dp

        return dp
    
    def calc_dp2(self):

        sim = self.sim

        pos = sim.getObjectPosition(self.coe, sim.handle_world)
        target_pos = sim.getObjectPosition(self.tip, sim.handle_world)

        pos_ang = sim.getObjectOrientation(self.coe, sim.handle_world)
        target_ang = sim.getObjectOrientation(self.tip, sim.handle_world)

        x_dp = target_pos[0] - pos[0]
        y_dp = target_pos[1] - pos[1]
        z_dp = target_pos[2] - pos[2]
        theta_dp = 0
        dp = np.empty((4,1))

        dp[0][0] = x_dp
        dp[1][0] = y_dp
        dp[2][0] = z_dp
        dp[3][0] = theta_dp

        return dp


    def calc_z_theta(self, theta):

        sim = self.sim

        pos_ang = sim.getObjectOrientation(self.coe, sim.handle_world)
        target_ang = sim.getObjectOrientation(self.tip, sim.handle_world)

        theta_dp = target_ang[2] - pos_ang[2]

        return theta_dp

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
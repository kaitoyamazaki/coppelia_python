from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import pandas as pd
import csv
import time

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
        self.cop = sim.getObject("/BaseRobot/CoP")
        self.robot = sim.getObject("/BaseRobot")

        self.l1 = 0.13156
        self.l2 = 0.1104
        self.l3 = 0.096
        self.l4 = 0.07318

        self.filepath = "../data/trapezoidal_control_y3.csv"
        self.df = pd.read_csv(self.filepath, header=None)
        self.data = self.df.values


        
    def simulation(self):
        
        sim = self.sim
        data = self.data

        sim.setStepping(True)
        sim.startSimulation()

        for i in range(len(data)):

            theta2 = sim.getJointPosition(self.j2)
            theta3 = sim.getJointPosition(self.j3)
            theta4 = sim.getJointPosition(self.j4)

            yakobi = self.calc_yakobi_row(theta2, theta3, theta4)
            yakobi_inv = np.linalg.inv(yakobi)

            theta = np.empty((1,3))
            theta[0][0] = theta2
            theta[0][1] = theta3
            theta[0][2] = theta4
            theta = theta.T
            theta_deg = np.rad2deg(theta)
            #print(f"{theta_deg[0][0]}, {theta_deg[1][0]}, {theta_deg[2][0]}")
            dp = self.calc_dp(data[i])

            #print(f"{dp.T}")

            new_theta = theta + np.dot(yakobi_inv, dp)
            new_theta_deg = np.rad2deg(new_theta)

            #sim.setJointPosition(self.j1, np.deg2rad(45))
            sim.setJointPosition(self.j2, new_theta[0][0])
            sim.setJointPosition(self.j3, new_theta[1][0])
            sim.setJointPosition(self.j4, new_theta[2][0])


            #print(f"{theta2}, {theta3}, {theta4}")
            #print(f"{yakobi}")
            #print(f"{yakobi_inv}")
            #print(f"{dp}")
            print(f"{new_theta_deg[0][0]-90}, {new_theta_deg[1][0]}, {new_theta_deg[2][0]}")


            sim.step()
            time.sleep(0.1)
        
        sim.stopSimulation()

        time.sleep(2)
    
    def calc_yakobi_row(self, j2, j3, j4):

        l2 = self.l2
        l3 = self.l3
        l4 = self.l4

        yakobi = np.empty((3,3))

        yakobi[0][0] = -l2 * np.sin(j2) - l3 * np.sin(j2+j3) - l4 * np.sin(j2+j3+j4)
        yakobi[0][1] = -l3 * np.sin(j2+j3) - l4 * np.sin(j2+j3+j4)
        yakobi[0][2] = -l4 * np.sin(j2+j3+j4)

        yakobi[1][0] = l2 * np.cos(j2) + l3 * np.cos(j2+j3) + np.cos(j2+j3+j4)
        yakobi[1][1] = l3 * np.cos(j2+j3) + np.cos(j2+j3+j4)
        yakobi[1][2] = np.cos(j2+j3+j4)

        yakobi[2][0] = 1
        yakobi[2][1] = 1
        yakobi[2][2] = 1

        return yakobi
    
    def calc_dp(self, data):

        sim = self.sim

        #print(f"{data}")
        pos = sim.getObjectPosition(self.cop, self.robot)
        y_dp = data[2] - pos[1]
        z_dp = 0
        theta_dp = 0.0
        dp = np.empty((3,1))
        dp[0][0] = y_dp
        dp[1][0] = z_dp
        dp[2][0] = theta_dp

        return dp



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
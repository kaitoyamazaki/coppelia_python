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

        self.j1 = sim.getObject("/robot/j1")
        self.j2 = sim.getObject("/robot/j2")
        self.j3 = sim.getObject("/robot/j3")
        self.pe = sim.getObject("/robot/pe")

        self.l1 = 0.0
        self.l2 = 0.4
        self.l3 = 0.2

        self.file_path = "../data/position_data.csv"
        self.df = pd.read_csv(self.file_path)
        self.data = self.df.values


    def simulation(self):

        sim = self.sim
        data = self.data

        sim.setStepping(True)
        sim.startSimulation()

        for i in range(len(data)):

            j1 = sim.getJointPosition(self.j1)
            j2 = sim.getJointPosition(self.j2)
            j3 = sim.getJointPosition(self.j3)

            yakobi = self.calc_yakobi(j1, j2, j3)
            yakobi_inv = np.linalg.inv(yakobi)

            theta = np.empty((3,1))
            theta[0][0] = j1
            theta[1][0] = j2
            theta[2][0] = j3

            theta_deg = np.rad2deg(theta)

            dp = self.calc_dp(data[i])

            new_theta = theta + np.dot(yakobi_inv, dp)
            new_theta_deg = np.rad2deg(new_theta)

            sim.setJointPosition(self.j1, new_theta[0][0])
            sim.setJointPosition(self.j2, new_theta[1][0])
            sim.setJointPosition(self.j3, new_theta[2][0])

            sim.step()
            time.sleep(0.1)
        
        sim.stopSimulation()
        time.sleep(2)

    

    def calc_yakobi(self, j1, j2, j3):

        l1 = self.l1
        l2 = self.l2
        l3 = self.l3

        yakobi = np.empty((3,3))

        yakobi[0][0] = np.sin(j1) * (l2 * np.sin(j2) + l3 * np.sin(j2 + j3))
        yakobi[0][1] = -np.cos(j1) * (l2 * np.cos(j2) + l3 * np.cos(j2 + j3))
        yakobi[0][2] = -l3 * np.cos(j1) * np.cos(j2 + j3)

        yakobi[1][0] = -np.cos(j1) * (l2 * np.sin(j2) + l3 * np.sin(j2 + j3))
        yakobi[1][1] = -np.sin(j1) * (l2 * np.cos(j2) + l3 * np.cos(j2 + j3))
        yakobi[1][2] = -l3 * np.sin(j1) * np.cos(j2 + j3)

        yakobi[2][0] = 0
        yakobi[2][1] = -l2 * np.sin(j2) - l3 * np.sin(j2 + j3)
        yakobi[2][2] = -l3 * np.sin(j2 + j3)

        return yakobi


    def calc_dp(self,data):

        sim = self.sim

        pos = sim.getObjectPosition(self.pe, sim.handle_world)

        x_dp = data[3] - pos[0]
        y_dp = data[4] - pos[1]
        z_dp = 0

        dp = np.empty((3,1))
        dp[0][0] = x_dp
        dp[1][0] = y_dp
        dp[2][0] = z_dp

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
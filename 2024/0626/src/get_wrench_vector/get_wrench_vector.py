# シミュレーション時のレンチベクトルを計算するための情報を取得する

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

        self.object = sim.getObject("/target_object")
        self.object_cog = sim.getObject("/target_object/cog")

        self.right_hand = sim.getObject("/BaseRobot/right_hand")
        self.left_hand = sim.getObject("/BaseRobot/left_hand")

        self.information = np.empty(0)

        self.l1 = 0.13156
        self.l2 = 0.1104
        self.l3 = 0.096
        self.l4 = 0.07318
        
    # シミュレーションに反映する関数
    def simulation(self):
        
        sim = self.sim
        sim.startSimulation()

        while sim.getSimulationTime() < 70:

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

            # ハンドの中心点(またはベース点)と物体重心の偏差を取得する関数
            self.get_information(sim)

            # ハンドの中心点の偏差とモーメントを計算するための位置ベクトルを取得する関数
            #self.get_information_moment(sim)
        
        sim.stopSimulation()

        reshape_information = self.information.reshape(-1, 5)
        #reshape_information_moment = self.information_moment.reshape(-1, 5)

        #print(f'{reshape_information}')
        #np.savetxt('data/まっすぐ並進運動時のデータ.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/まっすぐ並進運動時のデータ_土台を変更後.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/30度方向に並進運動時のデータ.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/30度方向に並進運動時のデータ_反対方向.csv', reshape_information, delimiter=',', fmt='%f')
        np.savetxt('data/斜めに並進運動時のデータ.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/斜めに並進運動時のデータ_反対方向.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/斜めに並進運動_回転運動時のデータ.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/斜めに並進運動時のデータ2.csv', reshape_information, delimiter=',', fmt='%f')
        #np.savetxt('data/斜めに並進運動時のデータ_target追加.csv', reshape_information, delimiter=',', fmt='%f')

        #print(f'{reshape_information_moment}')
        #np.savetxt('moment_data/まっすぐ並進運動時のデータ_位置ベクトルと位置偏差_ハンド中心.csv', reshape_information_moment, delimiter=',', fmt='%f')
        #np.savetxt('moment_data/まっすぐ並進運動時のデータ_位置ベクトルと位置偏差_理想値.csv', reshape_information_moment, delimiter=',', fmt='%f')

    # ヤコビ行列を計算する関数
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

    
    # 目標値と現在値の偏差を導出する関数
    def calc_dp(self, data):

        sim = self.sim

        pos = sim.getObjectPosition(self.coe, sim.handle_world)
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
    
    # 目標値と現在地の偏差を導出する関数（pathシステム用）
    def calc_dp2(self):

        sim = self.sim

        pos = sim.getObjectPosition(self.coe, sim.handle_world)
        target_pos = sim.getObjectPosition(self.tip, sim.handle_world)

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


    # 手先の姿勢のみを考慮する関数
    def calc_z_theta(self, theta):

        sim = self.sim

        pos_ang = sim.getObjectOrientation(self.coe, sim.handle_world)
        target_ang = sim.getObjectOrientation(self.tip, sim.handle_world)

        theta_dp = target_ang[2] - pos_ang[2]

        return theta_dp
    

    def get_information(self, sim):

        time = sim.getSimulationTime()
        
        # 全てワールド座標系であるとき
        #hand_pos = sim.getObjectPosition(self.coe, sim.handle_world)
        #cog_pos = sim.getObjectPosition(self.object_cog, sim.handle_world)
        #hand_pos = np.array(hand_pos)
        #cog_pos = np.array(cog_pos)
        #pos_vector = hand_pos - cog_pos

        # 物体座標系でやるとき
        hand_pos = sim.getObjectPosition(self.coe, self.object_cog)
        pos_vector = [hand_pos[0], hand_pos[1]]
        want_data = [time, hand_pos[0], hand_pos[1], pos_vector[0], pos_vector[1]]
        self.information = np.append(self.information, want_data)


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
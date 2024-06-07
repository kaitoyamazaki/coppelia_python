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

        # ハンドの力を取得
        self.right_hand_force = np.empty(0)
        self.left_hand_force = np.empty(0)

        # ハンドの位置を取得
        self.right_hand_pos = np.empty(0)
        self.left_hand_pos = np.empty(0)

        # 物体の重心, copの位置と姿勢を取得
        self.cog_pos = np.empty(0)
        self.cop_pos = np.empty(0)
        self.cop_ori = np.empty(0)
        self.cog_ori = np.empty(0)

        self.l1 = 0.13156
        self.l2 = 0.1104
        self.l3 = 0.096
        self.l4 = 0.07318
        
    # シミュレーションに反映する関数
    def simulation(self):
        
        sim = self.sim
        #data = self.data

        #sim.setStepping(True)
        sim.startSimulation()

        while sim.getSimulationTime() < 100:

            theta1 = sim.getJointPosition(self.j1)
            theta2 = sim.getJointPosition(self.j2)
            theta3 = sim.getJointPosition(self.j3)
            theta4 = sim.getJointPosition(self.j4)
            theta5 = sim.getJointPosition(self.j5)
            theta6 = sim.getJointPosition(self.j6)

            r_sensor = sim.getObject('/BaseRobot/right_sensor')
            l_sensor = sim.getObject('/BaseRobot/left_sensor')

            sim.setObjectOrientation(r_sensor, [0.0, 0.0, 0.0], sim.handle_world)
            sim.setObjectOrientation(l_sensor, [0.0, 0.0, 0.0], sim.handle_world)

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

            #self.get_object_pose()
            #self.check_collision()
            #self.output_cog_pos()
            #self.check_now_location(sim)
            self.test_force_sensor(sim)
            self.get_various_pos(sim)
        
        #sleep(5)

        sim.stopSimulation()

        #reshape_object_pose = self.object_pose.reshape(-1, 3)

        reshape_right_force = self.right_hand_force.reshape(-1, 3)
        reshape_left_force = self.left_hand_force.reshape(-1, 3)

        reshape_right_pos = self.right_hand_pos.reshape(-1, 3)
        reshape_left_pos = self.left_hand_pos.reshape(-1, 3)

        reshape_cog_pos = self.cog_pos.reshape(-1, 3)
        reshape_cop_pos = self.cop_pos.reshape(-1, 3)

        reshape_cog_ori = self.cog_ori.reshape(-1, 1)
        reshape_cop_ori = self.cop_ori.reshape(-1, 1)

        np.savetxt("data/test/force_r_typeA.csv", reshape_right_force, delimiter=",", fmt="%f")
        np.savetxt("data/test/force_l_typeA.csv", reshape_left_force, delimiter=",", fmt="%f")

        np.savetxt("data/test/right_pos_typeA.csv", reshape_right_pos, delimiter=",", fmt="%f")
        np.savetxt("data/test/left_pos_typeA.csv", reshape_left_pos, delimiter=",", fmt="%f")

        np.savetxt("data/test/cog_pos_typeA.csv", reshape_cog_pos, delimiter=",", fmt="%f")
        np.savetxt("data/test/cop_pos_typeA.csv", reshape_cop_pos, delimiter=",", fmt="%f")

        np.savetxt("data/test/cog_ori_typeA.csv", reshape_cog_ori, delimiter=",", fmt="%f")
        np.savetxt("data/test/cop_ori_typeA.csv", reshape_cop_ori, delimiter=",", fmt="%f")
    
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
    
    def get_object_pose(self):
        
        sim = self.sim
        pos = sim.getObjectPosition(self.object_cog, sim.handle_world)
        ori = sim.getObjectOrientation(self.object_cog, sim.handle_world)
        se2_object = [pos[0] * 1000, pos[1] * 1000, np.rad2deg(ori[2])]
        self.object_pose = np.append(self.object_pose, se2_object)
        #print(self.object_pose)
        #print(f"{se2_object[0]}, {se2_object[1]}, {se2_object[2]}")
    
    def check_collision(self):
        sim = self.sim

        res_right, handle_r = sim.checkCollision(self.object, self.right_hand)
        res_left, handle_l = sim.checkCollision(self.object, self.left_hand)
        time = sim.getSimulationTime()

        #print(f"res_left : {res_left}")

        #if res_left == 1:
            #print(f"{time} : 00")
        
        #if res_right == 1:
            #print(f"{time} : 1111")
    
    def output_cog_pos(self):

        sim = self.sim
        cog = sim.getObject("/target_object/cog")
        ori = sim.getObjectOrientation(cog, sim.handle_world)
        print(f"deg : {np.rad2deg(ori[2])}")

    
    def check_now_location(self, sim):

        right_hand = sim.getObject('/BaseRobot/right_hand')
        left_hand = sim.getObject('/BaseRobot/left_hand')
        object = sim.getObject('/target_object/cog')

        right_hand_pos = sim.getObjectPosition(right_hand, object)
        left_hand_pos = sim.getObjectPosition(left_hand, object)

        right_hand_pos = [round(pos, 5) for pos in right_hand_pos]
        left_hand_pos = [round(pos, 5) for pos in left_hand_pos]

        print(f'right hand : {right_hand_pos}')
        print(f'left hand : {left_hand_pos}')
    
    
    def test_force_sensor(self, sim):

        r_sensor = sim.getObject('/BaseRobot/right_sensor')
        l_sensor = sim.getObject('/BaseRobot/left_sensor')
        res, force, torque = sim.readForceSensor(r_sensor)
        res2, force2, torque2 = sim.readForceSensor(l_sensor)

        self.right_hand_force = np.append(self.right_hand_force, force)
        self.left_hand_force = np.append(self.left_hand_force, force2)
    

    def get_various_pos(self, sim):

        hand_r = sim.getObject('/BaseRobot/right_hand')
        hand_l = sim.getObject('/BaseRobot/left_hand')

        cog = sim.getObject('/target_object/cog')
        cop = sim.getObject('/BaseRobot/CoP')

        hand_pos_r = sim.getObjectPosition(hand_r, sim.handle_world)
        hand_pos_l = sim.getObjectPosition(hand_l, sim.handle_world)

        cog_pos = sim.getObjectPosition(cog, sim.handle_world)
        cop_pos = sim.getObjectPosition(cop, sim.handle_world)

        cog_ori = sim.getObjectOrientation(cog, sim.handle_world)
        cop_ori = sim.getObjectOrientation(cop, sim.handle_world)

        self.right_hand_pos = np.append(self.right_hand_pos, hand_pos_r)
        self.left_hand_pos = np.append(self.left_hand_pos, hand_pos_l)

        self.cog_pos = np.append(self.cog_pos, cog_pos)
        self.cop_pos = np.append(self.cop_pos, cop_pos)

        self.cog_ori = np.append(self.cog_ori, cog_ori[2])
        self.cop_ori = np.append(self.cop_ori, cop_ori[2])





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
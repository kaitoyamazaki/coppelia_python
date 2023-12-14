from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

class Simulation:

    def __init__(self): # ここでシミュレータ無いの物体ハンドルなどを取得, 目標位置の設定, 時間設定などを行う

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

        self.target_pos_x = 0.8
        self.target_pos_z = 0.8
        self.target_pos_theta = -90
        self.dp = 0.0001

        self.p_target = sim.getObject("/p_target")
        self.first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)

        self.first_deg_joint1 = sim.getJointPosition(self.joint1)
        self.first_deg_joint2= sim.getJointPosition(self.joint2)
        self.first_deg_joint3= sim.getJointPosition(self.joint3)
        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2 

        sim.setJointPosition(self.joint1, np.deg2rad(-1))
        sim.setJointPosition(self.joint2, np.deg2rad(0))
        sim.setJointPosition(self.joint3, np.deg2rad(0))

    def simulation(self):
        
        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        # 最終的な目標値の入力を行う
        target_pos = self.input_target_pos()

        # 目標位置と目標姿勢を表示
        sim.setObjectPosition(self.p_target, [target_pos[0][0], 0.0, target_pos[0][1]], sim.handle_world)
        sim.setObjectOrientation(self.p_target, [0.0, np.deg2rad(target_pos[0][2]), 0.0], sim.handle_world)
    
        while (t := sim.getSimulationTime()) < 500:

            # 現在の手先の位置情報を取得
            now_pe_pos = self.get_pe_pos_xz()

            # 目標位置に対しての進行方向を決定する
            direction = self.decide_direction(now_pe_pos, target_pos)

            # 次の時間周期でのpeの位置を導出する
            next_pe_pos = self.get_next_pe_pos(self.dp, direction, now_pe_pos)

            # ヤコビ行列を用いた逆運動学をするために現在の偏差を導出
            currently_dp = self.calc_dp(next_pe_pos, now_pe_pos)

            # ヤコビ行列を計算する
            yakobi = self.calc_yakobi()

            # 逆ヤコビ行列を導出する
            yakobi_inv = self.calc_yakobi_inv(yakobi)

            # 逆ヤコビ行列を元にt+1秒後のジョイント角度を計算する
            joint_t1_pos = self.calc_joint_next_pos(yakobi_inv, currently_dp)

            #print(f"{joint_t1_pos}")

            sim.setJointPosition(self.joint1, joint_t1_pos[0][0])
            sim.setJointPosition(self.joint2, joint_t1_pos[0][1])
            sim.setJointPosition(self.joint3, joint_t1_pos[0][2])

            print(f"now pe pos is : {now_pe_pos}")
            print(f"direction is : {direction}")
            print(f"next pe pos is : {next_pe_pos}")
            print(f"currently dp is : {currently_dp}")
            print(f"yakobi is : {yakobi}")
            print(f"inv of yakobi is : {yakobi_inv}")


            sim.step()
        
        sim.stopSimulation()

    # 目標値を設定する関数
    def input_target_pos(self):
    
        target_pos = np.empty((1,3))

        target_pos[0][0] = self.target_pos_x
        target_pos[0][1] = self.target_pos_z
        target_pos[0][2] = np.deg2rad(self.target_pos_theta)

        return target_pos
    
    # 手先の位置と姿勢を取得する関数
    def get_pe_pos_xz(self):

        sim = self.sim
        pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        ori = sim.getObjectOrientation(self.p_e, sim.handle_world)
        pos = [pos[0], pos[2], ori[1]]

        now_pe_pos = np.empty((1,3))
        for i in range(len(pos)):
            now_pe_pos[0][i] = pos[i]

        return now_pe_pos
    
    def decide_direction(self, now_pos, target_pos):

        sim = self.sim
        direction_flg = np.empty(3)

        for i in range(len(direction_flg)):

            if (target_pos[0][i] > now_pos[0][i]):
                direction_flg[i] = 1

            elif(target_pos[0][i] < now_pos[0][i]):
                direction_flg[i] = -1

            else:
                direction_flg[i] = 0

        return direction_flg

    def get_next_pe_pos(self, dp, direction, now_pos):

        next_pos = np.empty((1,3))

        for i in range(len(direction)):
            next_pos[0][i] = now_pos[0][i] + direction[i] * dp
        
        return next_pos
    
    def calc_dp(self, pe_t1, pe_t):
        
        dp = np.empty((1,3))
        for i in range(pe_t1.shape[1]):
            dp[0][i] = pe_t1[0][i] - pe_t[0][i]
        
        return dp
    
    def calc_yakobi(self):

        sim = self.sim

        l1 = self.l2
        l2 = self.l3
        l3 = self.l4

        theta = self.get_joint_position()

        #print(f"{theta}")

        #p_e = self.forward_kinematics()

        yakobi = np.empty((3,3))
        yakobi[0][0] = l1 * np.cos(theta[0][0]) + l2 * np.cos(theta[0][0] + theta[0][1]) + l3 * np.cos(theta[0][0] + theta[0][1] + theta[0][2])
        yakobi[0][1] = l2 * np.cos(theta[0][0] + theta[0][1]) + l3 * np.cos(theta[0][2])
        yakobi[0][2] = l3 * np.cos(theta[0][2])
        yakobi[1][0] = -l1 * np.sin(theta[0][0]) - l2 * np.sin(theta[0][0] + theta[0][1]) - l3 * np.sin(theta[0][0] + theta[0][1] + theta[0][2])
        yakobi[1][1] = -l2 * np.sin(theta[0][0] + theta[0][1]) - l3 * np.sin(theta[0][0] + theta[0][1] + theta[0][2])
        yakobi[1][2] = -l3 * np.sin(theta[0][2])
        yakobi[2][0] = 1
        yakobi[2][1] = 1
        yakobi[2][2] = 1

        return yakobi
    
    def get_joint_position(self):

        sim = self.sim
        theta = np.empty((1,3))

        theta[0][0] = sim.getJointPosition(self.joint1)
        theta[0][1] = sim.getJointPosition(self.joint2)
        theta[0][2] = sim.getJointPosition(self.joint3)

        return theta

    
    def forward_kinematics(self):

        sim = self.sim

        theta = self.get_joint_position()

        l1, l2, l3, theta1, theta2, theta3 = sp.symbols("l1 l2 l3 theta1 theta2 theta3")
        xe = l1 * sp.cos(theta1) + l2 * sp.cos(theta1 + theta2) + l3 * sp.cos(theta1 + theta2 +theta3)
        ye = l1 * sp.sin(theta1) + l2 * sp.sin(theta1 + theta2) + l3 * sp.sin(theta1 + theta2 + theta3)
        theta_e = theta1 + theta2 + theta3

        forward_pos = [xe, ye, theta_e]

        values_of_robot = {
            l1: self.l2,
            l2: self.l3,
            l3: self.l4,
            theta1: theta[0][0],
            theta2: theta[0][1],
            theta3: theta[0][2]
        }

        yakobi = np.empty((0,3))

        for i in range(len(forward_pos)):
            x_dot = sp.diff(forward_pos[i], theta1)
            x_dot = float(x_dot.subs(values_of_robot))
            y_dot = sp.diff(forward_pos[i], theta2)
            y_dot = float(y_dot.subs(values_of_robot))
            theta_dot = sp.diff(forward_pos[i], theta3)
            theta_dot = float(theta_dot.subs(values_of_robot))
            line = [x_dot, y_dot, theta_dot]
            yakobi = np.vstack((yakobi, line))
        
        return yakobi

    def calc_yakobi_inv(self, yakobi):

        return np.linalg.inv(yakobi)
    
    def calc_joint_next_pos(self, inv, dp):

        sim = self.sim
        theta = self.get_joint_position()
        now_theta = theta.T

        use_dp = dp.T

        #print(f"{use_dp}")

        dtheta = np.dot(inv, use_dp)
        dtheta[0][0] = -1 * dtheta[0][0]
        print(f"dtheta is : {np.rad2deg(dtheta).T}")

        next_theta = now_theta + dtheta

        #test = next_theta.T

        print(f"next theta is : {np.rad2deg(next_theta).T}")

        return next_theta.T


def main():
    simulation = Simulation()
    simulation.simulation()


if __name__ == '__main__':

    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
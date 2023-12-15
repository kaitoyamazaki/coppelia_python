from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

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
        self.joint3 = sim.getObject("/base/joint/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/joint/link1/joint/link2/joint/link3")
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/joint/link3/p_e")

        self.target_pos_x = -0.9
        self.target_pos_y = 1.2
        self.target_pos_theta = 175
        self.dp = 0.001

        self.p_t = sim.getObject("/p_t")
        self.first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)

        self.l1 = 1.0
        self.l2 = 0.5
        self.l3 = 0.5
    
    # シミュレーションを実施する関数
    def simulation(self):

        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        pos_of_p_t = self.assign_p_t_pos()

        # 目標位置と姿勢を表示

        sim.setObjectPosition(self.p_t, [pos_of_p_t[0][0], pos_of_p_t[0][1], 0.05], sim.handle_world)
        sim.setObjectOrientation(self.p_t, [0.0, 0.0, np.deg2rad(self.target_pos_theta)], sim.handle_world)

        while (t := sim.getSimulationTime()) < 2000:

            # ヤコビ行列を計算する
            yakobi = self.calc_yakobi()

            # 逆ヤコビ行列を計算する
            yakobi_inv = self.calc_yakobi_inv(yakobi)

            # 現在の手先に関する位置情報を取得
            pe_pos = self.get_pe_pos_xy()

            # 目標位置に対しての進行方向を決定する
            direction = self.decide_direction(pe_pos, pos_of_p_t)

            # 次時間軸での手先の位置を導出
            pos_of_pe_t1 = self.calc_pos_pe_t1(self.dp, direction, pe_pos)

            # 次の時間軸と現在の時間軸の偏差を計算する
            currently_dp = self.calc_dp(pos_of_pe_t1, pe_pos)

            # 逆ヤコビ行列を使って, 次の角度を導出する
            theta_pos = self.calc_theta_t1(yakobi_inv, currently_dp)


            sim.setJointPosition(self.joint1, theta_pos[0][0])
            sim.setJointPosition(self.joint2, theta_pos[1][0])
            sim.setJointPosition(self.joint3, theta_pos[2][0])

            print(f"yakobi : {yakobi}")
            print(f"yakobi inv : {yakobi_inv}")
            print(f"pos of p_t : {pos_of_p_t}")
            print(f"pos of p_e : {pe_pos}")
            print(f"direction : {direction}")
            print(f"currently dp : {currently_dp}")

            sim.step()
        
        sim.stopSimulation()


    # 目標位置・姿勢を代入する関数
    def assign_p_t_pos(self):
        
        pos_of_p_t = np.empty((1,3))

        pos_of_p_t[0][0] = self.target_pos_x
        pos_of_p_t[0][1] = self.target_pos_y
        pos_of_p_t[0][2] = np.deg2rad(self.target_pos_theta)

        return pos_of_p_t
    

    def get_pe_pos_xy(self):

        sim = self.sim
        
        p_e_pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        p_e_ori = sim.getObjectOrientation(self.p_e, sim.handle_world)

        pos = [p_e_pos[0], p_e_pos[1], p_e_ori[2]]

        p_e_posture = np.empty((1,3))
        
        for i in range(len(pos)):

            p_e_posture[0][i] = pos[i]
        
        return p_e_posture


    def decide_direction(self, pos_of_p_e, pos_of_p_t):

        sim = self.sim
        direction_flg = np.empty(3)

        for i in range(len(direction_flg)):

            if(pos_of_p_t[0][i] > pos_of_p_e[0][i]):
                direction_flg[i] = 1
            
            elif(pos_of_p_t[0][i] < pos_of_p_e[0][i]):
                direction_flg[i] = -1
            
            else:
                direction_flg[i] = 0
        
        return direction_flg

    
    def calc_pos_pe_t1(self, dp, direction, pe_pos):

        pos_of_pe_t1 = np.empty((1,3))

        for i in range(len(direction)):
            pos_of_pe_t1[0][i] = pe_pos[0][i] + direction[i] * dp
        
        return pos_of_pe_t1
    
    def calc_dp(self, p_t1, p_t):

        dp = np.empty((1,3))

        for i in range(p_t.shape[1]):
            dp[0][i] = p_t1[0][i] - p_t[0][i]

        return dp

    
    def calc_yakobi(self):

        sim = self.sim

        l1 = self.l1
        l2 = self.l2
        l3 = self.l3

        theta = self.get_joint_position()
        print(f"theta is {theta}")

        yakobi = np.empty((3,3))

        yakobi[0][0] = -l1 * np.sin(theta[0]) - l2 * np.sin(theta[0] + theta[1]) - l3 * np.sin(theta[0] + theta[1] + theta[2])
        yakobi[0][1] = - l2 * np.sin(theta[0] + theta[1]) - l3 * np.sin(theta[0] + theta[1] + theta[2])
        yakobi[0][2] = - l3 * np.sin(theta[0] + theta[1] + theta[2])

        yakobi[1][0] = l1 * np.cos(theta[0]) + l2 * np.cos(theta[0] + theta[1]) + l3 * np.cos(theta[0] + theta[1] + theta[2])
        yakobi[1][1] = l2 * np.cos(theta[0] + theta[1]) + l3 * np.cos(theta[0] + theta[1] + theta[2])
        yakobi[1][2] = l3 * np.cos(theta[0] + theta[1] + theta[2])

        yakobi[2][0] = 1
        yakobi[2][1] = 1
        yakobi[2][2] = 1

        return yakobi


    def get_joint_position(self):

        sim = self.sim
        theta = np.empty(3)

        theta[0] = sim.getJointPosition(self.joint1)
        theta[1] = sim.getJointPosition(self.joint2)
        theta[2] = sim.getJointPosition(self.joint3)

        return theta
    
    def calc_yakobi_inv(self, yakobi):

        return np.linalg.inv(yakobi)
    

    def calc_theta_t1(self,yakobi_inv, dp):

        theta = self.get_joint_position_use_yakobi()
        theta_t1 = theta.T + np.dot(yakobi_inv, dp.T)

        print(f"theta_t+1 : {theta_t1}")

        return theta_t1


    def get_joint_position_use_yakobi(self):

        sim = self.sim
        theta = np.empty((1,3))

        theta[0][0] = sim.getJointPosition(self.joint1)
        theta[0][1] = sim.getJointPosition(self.joint2)
        theta[0][2] = sim.getJointPosition(self.joint3)

        return theta

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
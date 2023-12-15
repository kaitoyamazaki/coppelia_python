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
        self.joint1 = sim.getObject("/base/ForceSensor/link1/joint")
        self.link2 = sim.getObject("/base/ForceSensor/link1/joint/link2")
        self.joint2 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3")
        self.joint3 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint")
        self.link4 = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4")
        self.p_e = sim.getObject("/base/ForceSensor/link1/joint/link2/joint/link3/joint/link4/p_e")

        self.p_t = sim.getObject("/p_target")

        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2

        self.p_t_x = 0.8
        self.p_t_z = 0.4
        self.p_t_theta = 0.0
        self.dp = 0.0001

    
    def simulation(self):

        sim = self.sim
        sim.setStepping(True)
        sim.startSimulation()

        pos_of_p_t = self.assign_p_t()

        # 目標位置と目標姿勢を記述

        sim.setObjectPosition(self.p_t, [pos_of_p_t[0][0], 0.0, pos_of_p_t[0][1]], sim.handle_world)
        sim.setObjectOrientation(self.p_t, [0.0, pos_of_p_t[0][2] + np.deg2rad(90), 0.0], sim.handle_world)

        # ヤコビ行列
        yakobi = self.calc_yakobi()

        # 逆ヤコビアン
        yakobi_inv =  self.calc_yakobi_inv(yakobi)

        # 現在の手先位置・姿勢を導出
        pe_pos = self.get_pe_pos_xz()

        # 目標位置に対しての進行方向を決定する
        direction = self.decide_direction(pe_pos, pos_of_p_t)

        # 次時間軸での手先の位置を導出
        pos_of_pe_t1 = self.calc_pos_pe_t1(self.dp, direction, pe_pos)

        # 偏差を計算する
        currently = self.calc_dp(pos_of_pe_t1, pe_pos)

        # 偏差を利用して逆ヤコビアンを用いた計算を行う
        theta_pos = self.calc_theta_t1(yakobi_inv, currently_dp) 

        

        print(f"yakobi : {yakobi}")
        print(f"yakobi inv : {yakobi_inv}")
        print(f"pos of pt : {pos_of_p_t}")
        print(f"pos of pe : {pe_pos}")
        print(f"direction : {direction}")
        print(f"currently dp : {currently}")

        while (t := sim.getSimulationTime()) < 10:

            ## ヤコビ行
            #yakobi = self.calc_yakobi()

            ## 逆ヤコビアン
            #yakobi_inv =  self.calc_yakobi_inv(yakobi)

            #print(yakobi)
            ##print(yakobi_inv)

            sim.step()
        
        sim.stopSimulation()
    
    
    def assign_p_t(self):

        pos_of_p_t = np.empty((1,3))

        pos_of_p_t[0][0] = self.p_t_x
        pos_of_p_t[0][1] = self.p_t_z
        pos_of_p_t[0][2] = np.deg2rad(self.p_t_theta)

        return pos_of_p_t
    
    def calc_yakobi(self):

        sim = self.sim

        theta = self.get_joint_position()
        print(theta)

        l1, l2, l3, j1, j2, j3 = sp.symbols("l1 l2 l3 j1 j2 j3")
        xe = l1 * sp.cos(j1) + l2 * sp.cos(j1 + j2) +l3 * sp.cos(j1 + j2 + j3)
        ze = l1 * sp.sin(j1) + l2 * sp.sin(j1+j2) + l3 * sp.sin(j1 + j2 + j3)
        j_e = j1 + j2 + j3
        
        forward_pos = [xe, ze, j_e]

        values_of_robot = {
            l1 : self.l2,
            l2 : self.l3,
            l3 : self.l4,
            j1 : theta[0],
            j2 : theta[1],
            j3 : theta[2]
        }

        yakobi = np.empty((0,3))

        for i in range(len(forward_pos)):

            j1_dot = sp.diff(forward_pos[i], j1)
            j1_dot = float(j1_dot.subs(values_of_robot))
            j2_dot = sp.diff(forward_pos[i], j2)
            j2_dot = float(j2_dot.subs(values_of_robot))
            j3_dot = sp.diff(forward_pos[i], j3)
            j3_dot = float(j3_dot.subs(values_of_robot))

            line = [j1_dot, j2_dot, j3_dot]
            yakobi = np.vstack((yakobi, line))
        
        return yakobi


    def calc_yakobi_inv(self, yakobi):

        return np.linalg.inv(yakobi)
    

    def get_joint_position(self):

        sim = self.sim

        theta = np.empty(3)

        theta[0] = sim.getJointPosition(self.joint1)
        theta[1] = sim.getJointPosition(self.joint2)
        theta[2] = sim.getJointPosition(self.joint3)

        return theta
    
    
    def get_pe_pos_xz(self):

        sim = self.sim
        pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        ori = sim.getObjectOrientation(self.p_e, sim.handle_world)

        pos_of_p_e = [pos[0], pos[2], ori[1]]

        posuture_of_p_e = np.empty((1,3))

        for i in range(len(pos)):
            posuture_of_p_e[0][i] = pos_of_p_e[i]

        return posuture_of_p_e
    

    def decide_direction(self, pe, pt):

        sim = self.sim
        direction_flg = np.empty(3)

        for i in range(len(direction_flg)):

            if(pt[0][i] > pe[0][i]):
                direction_flg[i] = 1
            
            elif(pt[0][i] < pe[0][i]):
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

        for i in range(p_t1.shape[1]):
            dp[0][i] = p_t1[0][i] - p_t[0][i]

        return dp
    

    def calc_theta_t1(self, yakobi_inv, dp):
        pass
        

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
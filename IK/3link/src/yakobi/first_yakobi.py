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

        self.target_pos_x = 0.8
        self.target_pos_y = 0.8
        self.target_pos_theta = 0
        self.dp = 0.0001

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
        sim.setObjectOrientation(self.p_t, [np.deg2rad(self.target_pos_theta), 0.0, 0.0], sim.handle_world)

        while (t := sim.getSimulationTime()) < 50:

            # 現在の手先に関する位置情報を取得
            now_pe_pos = self.get_pe_pos_xy()

            print(f"{now_pe_pos}")

    # 目標位置・姿勢を代入する関数
    def assign_p_t_pos(self):
        
        pos_of_p_t = np.empty((1,3))

        pos_of_p_t[0][0] = self.target_pos_x
        pos_of_p_t[0][1] = self.target_pos_y
        pos_of_p_t[0][2] = self.target_pos_theta

        return pos_of_p_t
    
    def get_pe_pos_xy(self):

        sim = self.sim
        
        p_e_pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        p_e_ori = sim.getObjectOrientation(self.p_e, sim.handle_world)

        pos = [p_e_pos[0], p_e_pos[1], p_e_ori[0]]

        p_e_posture = np.empty((1,3))
        
        for i in range(len(pos)):

            p_e_posture[0][i] = pos[i]
        
        return p_e_posture



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
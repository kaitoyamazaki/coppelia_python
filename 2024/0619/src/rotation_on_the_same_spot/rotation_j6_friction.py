# 対象物体をTypeBの状態でその場回転させるプログラム
# そのうえで部分的な摩擦力の計算も行う
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

        # 部分的な重心のハンドルを取得
        self.cog1 = sim.getObject('/target_object/cog_1')
        self.cog2 = sim.getObject('/target_object/cog_2')
        self.cog3 = sim.getObject('/target_object/cog_3')
        self.cog4 = sim.getObject('/target_object/cog_4')
        self.cog5 = sim.getObject('/target_object/cog_5')
        self.cog6 = sim.getObject('/target_object/cog_6')
        self.cog7 = sim.getObject('/target_object/cog_7')
        self.cog8 = sim.getObject('/target_object/cog_8')

        # 別に設定した重心を格納する行列
        self.cog = np.empty(0)
        self.old_cog = np.empty(0)
        self.friction_dp = np.empty(0)
        self.friction_flg = 1

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

            theta6 = sim.getJointPosition(self.j6)
            z_new_theta = self.calc_j6(sim, theta6)

            sim.setJointPosition(self.j6, z_new_theta)
            self.get_cog_information(sim)

        #sleep(5)

        sim.stopSimulation()
        reshape_friction_dp = self.friction_dp.reshape(-1, 17)

        np.savetxt("data/test/partially_friction_points.csv", reshape_friction_dp, delimiter=",", fmt="%f")


    def calc_j6(self, sim, theta):

        theta = np.rad2deg(theta)
        theta = theta + 0.5
        #print(f'theta : {theta}')
        theta = np.deg2rad(theta)

        return theta

    
    def get_cog_information(self, sim):

        time = sim.getSimulationTime()
        cog1_pos = sim.getObjectPosition(self.cog1, sim.handle_world)
        cog2_pos = sim.getObjectPosition(self.cog2, sim.handle_world)
        cog3_pos = sim.getObjectPosition(self.cog3, sim.handle_world)
        cog4_pos = sim.getObjectPosition(self.cog4, sim.handle_world)
        cog5_pos = sim.getObjectPosition(self.cog5, sim.handle_world)
        cog6_pos = sim.getObjectPosition(self.cog6, sim.handle_world)
        cog7_pos = sim.getObjectPosition(self.cog7, sim.handle_world)
        cog8_pos = sim.getObjectPosition(self.cog8, sim.handle_world)

        cog_pos = [cog1_pos[0], cog1_pos[1], cog2_pos[0], cog2_pos[1], cog3_pos[0], cog3_pos[1], cog4_pos[0], cog4_pos[1], cog5_pos[0], cog5_pos[1], cog6_pos[0], cog6_pos[1], cog7_pos[0], cog7_pos[1], cog8_pos[0], cog8_pos[1]]
            
        if(self.friction_flg == 1):
            self.friction_flg = 0
            self.old_cog = cog_pos
            
        cog_pos = np.array(cog_pos)
        self.old_cog = np.array(self.old_cog)
            
        dp = cog_pos - self.old_cog

        dp = np.insert(dp, 0, time)

        #print(f'dp : {dp}')
        self.friction_dp = np.append(self.friction_dp, dp)
        #print(f'{self.friction_dp.shape}')

        self.old_cog = cog_pos


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
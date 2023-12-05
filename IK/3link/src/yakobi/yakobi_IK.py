from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

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

        self.target_pos_x = 1.3
        self.target_pos_z = 0.4
        self.dp = 0.001

        self.p_target = sim.getObject("/p_target")
        self.first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)

        self.first_deg_joint1 = sim.getJointPosition(self.joint1)
        self.first_deg_joint2= sim.getJointPosition(self.joint2)
        self.first_deg_joint3= sim.getJointPosition(self.joint3)
        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2 

    def simulation(self):
        
        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        # 最終的な目標値の入力を行う
        target_pos = self.input_target_pos()

        # 目標位置表示
        sim.setObjectPosition(self.p_target, [target_pos[0][0], 0.0, target_pos[0][1]], sim.handle_world)
    
        while (t := sim.getSimulationTime()) < 10:

            # 現在の手先の位置情報を取得
            now_pe_pos = self.get_pe_pos_xz()

            # 目標位置に対しての進行方向を決定する
            direction = self.decide_direction(now_pe_pos, target_pos)

            # 次の時間周期でのpeの位置を導出する
            next_pe_pos = self.get_next_pe_pos(self.dp, direction, now_pe_pos)

            print(f"{next_pe_pos}")


            sim.step()
        
        sim.stopSimulation()

    def input_target_pos(self):
    
        target_pos = np.empty((1,2))

        target_pos[0][0] = self.target_pos_x
        target_pos[0][1] = self.target_pos_z

        return target_pos
    
    def get_pe_pos_xz(self):

        sim = self.sim
        pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        pos = [pos[0], pos[2]]

        now_pe_pos = np.empty((1,2))
        for i in range(len(pos)):
            now_pe_pos[0][i] = pos[i]

        return now_pe_pos
    
    def decide_direction(self, now_pos, target_pos):

        sim = self.sim
        direction_flg = np.empty(2)

        for i in range(len(direction_flg)):

            if (target_pos[0][i] > now_pos[0][i]):
                direction_flg[i] = 1

            elif(target_pos[0][i] < now_pos[0][i]):
                direction_flg[i] = -1

            else:
                direction_flg[i] = 0

        return direction_flg

    def get_next_pe_pos(self, dp, direction, now_pos):

        next_pos = np.empty((1,2))

        for i in range(len(direction)):
            next_pos[0][i] = now_pos[0][i] + direction[i] * dp
        
        return next_pos

def main():
    simulation = Simulation()
    simulation.simulation()


if __name__ == '__main__':

    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
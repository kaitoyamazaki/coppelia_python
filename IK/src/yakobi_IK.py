from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import time

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
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/p_end")

        self.target_pos_x = 0.7
        self.target_pos_y = 1.2
        self.dp = 0.001

        self.p_target = sim.getObject("/p_target")
        self.first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)

        #self.camera = sim.getObject("/Camera")
        #sim.setObjectPosition(self.camera, [0, 0, 10])

        self.first_deg_joint1 = sim.getJointPosition(self.joint1)
        self.first_deg_joint2= sim.getJointPosition(self.joint2)
        self.l1 = 1
        self.l2 = 0.5

    
    def simulation(self): ## シミュレーションを実施している関数, 基本は全てこの関数で処理している

        sim = self.sim

        sim.setStepping(True)
        sim.startSimulation()

        # 初期位置の取得
        first_pos = self.get_first_pos()
        target_pos = self.input_target() ##最終的な目標値を入力する
        ##初期の進行方向を決定する
        #direction = self.decide_direction(target_pos, first_pos)

        # 最終的な目標地点をシミュレーション空間に描画
        sim.setObjectPosition(self.p_target, [target_pos[0][0], target_pos[0][1], 0.05], sim.handle_world)


        while (t := sim.getSimulationTime()) < 50:

            # 現在の手先位置を取得
            now_pe_pos = self.get_pe_pos()

            # 現在の位置からの進行方向を決定する
            direction = self.decide_direction(target_pos, now_pe_pos)

            # 次の場所を導出
            next_pe_pos = self.get_next_pe(self.dp, direction, now_pe_pos)

            # ヤコビ行列を適用するための位置に関する偏差を導出
            currentry_dp = self.get_dp(next_pe_pos, now_pe_pos)

            

            #print(f"direction is {direction}")
            #print(f"next_pe is {next_pe_pos}")
            #print(f"currentry_dp is {currentry_dp}")
            sim.step()
        
        sim.stopSimulation()

    def get_first_pos(self):

        sim = self.sim
        first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        numpy_first_pos = np.empty((1,2))
        numpy_first_pos[0][0] = first_pos[0]
        numpy_first_pos[0][1] = first_pos[1]

        return numpy_first_pos


    
    def input_target(self): #目標値を設定する関数, 最悪変数はグローバル化でも良いかも

        target_pos = np.empty((1,2))

        target_pos[0][0] = self.target_pos_x
        target_pos[0][1] = self.target_pos_y

        #x, y = map(float, input("Enter x, y of the Endeffector : ").split(','))

        return target_pos

    # 進行方向の決定する関数
    def decide_direction(self, target_pos, now_pos):

        sim = self.sim
        direction_flg = np.empty((1,2))

        # for分でまとめる
        if (target_pos[0][0] > now_pos[0][0]):
            direction_flg[0][0] = 1

        elif(target_pos[0][0] < now_pos[0][0]):
            direction_flg[0][0] = -1
        
        else:
            direction_flg[0][0] = 0

        
        if (target_pos[0][1] > now_pos[0][1]):
            direction_flg[0][1] = 1

        elif(target_pos[0][1] < now_pos[0][1]):
            direction_flg[0][1] = -1

        else:
            direction_flg[0][1] = 0


        return direction_flg

        
    def get_pe_pos(self): ## エンドエフェクタp_eの座標を2次元で取得する関数
        
        sim = self.sim
        pe_pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        pe_pos_xy = np.empty((1,2))

        pe_pos_xy[0][0] = pe_pos[0]
        pe_pos_xy[0][1] = pe_pos[1]

        return pe_pos_xy

    
    def get_next_pe(self, dp, direction, now_pos):

        dx = direction[0][0] * dp
        dy = direction[0][1] * dp

        #print(f"dx, dy is ({dx}, {dy})")

        next_pos = np.empty((1,2))
        next_pos[0][0] = now_pos[0][0] + dx
        next_pos[0][1] = now_pos[0][1] + dy

        return next_pos


    def get_dp(self, t_i1, t_i):

        dp = np.empty((1,2))
        dp[0][0] = t_i1[0][0] - t_i[0][0]
        dp[0][1] = t_i1[0][1] - t_i[0][1]

        return dp
    
    #def get_div_pos(self, x, y):
        #l1 = self.l1
        #l2 = self.l2

        #first_x = l1 * np.cos(0) + l2 * np.cos(np.deg2rad(0+90))
        #first_y = l1 * np.sin(0) + l2 * np.sin(np.deg2rad(0+90))

        #dx = x - first_x
        #dy = y - first_y

        #dq = np.empty((2,1))
        #dq[0][0] = dx
        #dq[1][0] = dy

        #print(f"{dq}")

        #return dq


    #def input_target(self): #目標値を設定する関数, 最悪変数はグローバル化でも良いかも

        #target_pos = np.empty((1,2))

        #target_pos[0][0] = self.target_pos_x
        #target_pos[0][1] = self.target_pos_y

        ##x, y = map(float, input("Enter x, y of the Endeffector : ").split(','))

        #return target_pos



    # ここからは使わない予定の関数, 今後削除の予定

    #def IK(self, j1, j2, dq):
        #l1 = self.l1
        #l2 = self.l2

        #now_rad = self.get_now_joint()

        #first_IK = self.calc_IK(l1, l2, j1, j2)

        #result = np.dot(first_IK, dq)

        #result = now_rad + result

        #print(f"result is {np.rad2deg(result)}")

        #return result



    
    #def get_now_joint(self):
        #now_joint = np.empty((2,1))
        #now_joint[0][0] = self.first_deg_joint1
        #now_joint[1][0] = self.first_deg_joint2

        #print(f"{now_joint}")

        #return now_joint
    
    #def calc_IK(self, l1, l2, j1, j2):
        #IK_queue = np.empty((2,2))
        #IK_queue[0][0] = (l2 * np.cos(j1 + j2)) / (l1 * l2 * np.sin(j2))
        #IK_queue[0][1] = (l2 * np.sin(j1 + j2)) / (l1 * l2 * np.sin(j2))
        #IK_queue[1][0] = (-l1 * np.cos(j1) - l2 * np.cos(j1 + j2)) / (l1 * l2 * np.sin(j2))
        #IK_queue[1][1] = (-l1 * np.sin(j1) - l2 * np.sin(j1 + j2)) / l1 * l2 * np.sin(j2)

        #return IK_queue

    
def main():
    simulator = Simulation()
    simulator.simulation()
    

if __name__ == '__main__':
    
    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
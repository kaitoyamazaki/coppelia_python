from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

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

            # ヤコビ行列を導出する
            yakobi = self.get_yakobi()

            # 逆ヤコビ行列を導出する
            yakobi_inv = self.get_yakobi_inv(yakobi)

            # 逆ヤコビ行列をもとに, t+1病後の角度を求める
            joint_pos_next = self.get_joint_pos_next(yakobi_inv, currentry_dp)

            sim.setJointPosition(self.joint1, joint_pos_next[0][0])
            sim.setJointPosition(self.joint2, joint_pos_next[0][1])
            


            # 標準出力を出す！！！
            #print(f"direction is {direction}")
            #print(f"next_pe is {next_pe_pos}")
            #print(f"currentry_dp is {currentry_dp}")
            #print(f"joint pos is {yakobi}")
            #print(f"yakobi is {yakobi}")
            #print(f"yakobi inv is {yakobi_inv}")
            sim.step()
        
        sim.stopSimulation()

    def get_first_pos(self):

        sim = self.sim
        first_pos = sim.getObjectPosition(self.p_e, sim.handle_world)
        numpy_first_pos = np.empty((1,2))
        #numpy_first_pos[0][0] = first_pos[0]
        #numpy_first_pos[0][1] = first_pos[1]

        for i in range(numpy_first_pos.shape[1]):
            numpy_first_pos[0][i] = first_pos[i]

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

        for i in range(pe_pos_xy.shape[1]):
            pe_pos_xy[0][i] = pe_pos[i]

        return pe_pos_xy

    
    def get_next_pe(self, dp, direction, now_pos):

        next_pos = np.empty((1,2))

        for i in range(direction.shape[1]):
            next_pos[0][i] = now_pos[0][i] + direction[0][i] * dp

        return next_pos


    def get_dp(self, t_i1, t_i):

        dp = np.empty((1,2))
        for i in range(t_i1.shape[1]):
            dp[0][i] = t_i1[0][i] - t_i[0][i]

        return dp
    

    # ジョイントの角度を求める機能
    def get_joint_position(self):

        sim = self.sim

        joint_pos = np.empty((1,2))
        joint_pos[0][0] = sim.getJointPosition(self.joint1)
        joint_pos[0][1] = sim.getJointPosition(self.joint2)

        return joint_pos


    def get_yakobi(self):

        l1 = self.l1
        l2 = self.l2

        joint = self.get_joint_position()

        yakobi = np.empty((2, 2))
        yakobi[0][0] = -l1 * np.sin(joint[0][0]) - l2 * np.sin(joint[0][0] + joint[0][1])
        yakobi[0][1] = -l2 * np.sin(joint[0][0] + joint[0][1])
        yakobi[1][0] = l1 * np.cos(joint[0][0]) + l2 * np.cos(joint[0][0] + joint[0][1])
        yakobi[1][1] = l2 * np.cos(joint[0][0] + joint[0][1])

        return yakobi

    
    def get_yakobi_inv(self, yakobi):

        return np.linalg.inv(yakobi)
    
    def get_joint_pos_next(self, yakobi_inv, dp):

        sim = self.sim

        joint = self.get_joint_position()
        now_joint = joint.T
        
        use_dp = dp.T
        dtheta = np.dot(yakobi_inv, use_dp)

        next_theta = now_joint + dtheta

        return next_theta.T

    
def main():
    simulator = Simulation()
    simulator.simulation()
    

if __name__ == '__main__':
    
    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによるプログラム停止")
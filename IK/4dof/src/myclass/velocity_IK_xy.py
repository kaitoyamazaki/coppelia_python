from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

class IK_XY():

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        # モデルの情報を取得
        self.joint1 = sim.getObject("/base/joint")
        #self.joint2 = sim.getObject("/base/joint/link1/joint")
        #self.joint3 = sim.getObject("/base/joint/link1/joint/link2/joint")
        #self.joint4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint")
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4/p_e")

        self.pt_x = 1.1
        self.pt_y = 0.4
        self.pt_z = 0.4
        self.pt_theta = 0.0
        self.target_xy_theta = np.arctan2(self.pt_y, self.pt_x)

        self.dp = 0.001

    def IK(self):

        sim = self.sim

        # xy平面における目標位置を代入
        pos_of_pt = self.assign_pt_pos()

        # 現時点での手先の位置を取得
        pos_of_pe = self.get_pos_of_pe()

        # 進行方向を決定する
        direction = self.decide_direction(pos_of_pe, pos_of_pt)

        # 次時間軸での手先の位置を計算
        pos_of_pe_t1 = self.calc_pos_pe_t1(self.dp, direction, pos_of_pe)

        # 次時間軸での手先の位置と現在の手先の位置の偏差を計算
        currently_dp = self.calc_dp(pos_of_pe, pos_of_pe_t1)

        #次時間での角度を導出
        theta = self.calc_j1_theta(pos_of_pe, pos_of_pe_t1)


        #print(f"pos_of_pe : {pos_of_pe}")
        #print(f"pos of pt : {pos_of_pt}")
        #print(f"direction : {direction}")
        #print(f"pos of pe_t1 : {pos_of_pe_t1}")
        #print(f"currently dp : {currently_dp}")
        print(f"theta : {theta}")

        return theta


    def assign_pt_pos(self):

        pos_of_pt = np.empty(2)

        pos_of_pt[0] = self.pt_x
        pos_of_pt[1] = self.pt_y

        return pos_of_pt

    
    def get_pos_of_pe(self):

        sim = self.sim

        pos_of_pe = sim.getObjectPosition(self.p_e, sim.handle_world)

        posture_of_pe = [pos_of_pe[0], pos_of_pe[1]]
        
        return posture_of_pe

    
    def decide_direction(self, pe, pt):

        direction_flg = np.empty(2)

        for i in range(len(direction_flg)):
            
            if(pt[i] > pe[i]):
                direction_flg[i] = 1
            
            elif(pt[i] < pe[i]):
                direction_flg[i] = -1
            
            else:
                direction_flg[i] = 0

        return direction_flg
    
    
    def calc_pos_pe_t1(self, dp, direction, pe):

        pos_of_pe_p1 = np.empty(2)

        for i in range(len(direction)):
            pos_of_pe_p1[i] = pe[i] + direction[i] * dp
        
        return pos_of_pe_p1
    
    def calc_dp(self, pe, pe_t1):

        dp = np.empty(2)
        
        for i in range(len(dp)):
            dp[i] = pe_t1[i] - pe[i]

        return dp
    
    
    def calc_j1_theta(self, pe, pe_t1):

        theta = np.arctan2(pe_t1[1], pe_t1[0])

        if (theta > self.target_xy_theta):
            theta = self.target_xy_theta
        
        return theta
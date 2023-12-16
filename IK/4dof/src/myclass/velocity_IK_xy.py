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
        #self.joint1 = sim.getObject("/base/joint")
        #self.joint2 = sim.getObject("/base/joint/link1/joint")
        #self.joint3 = sim.getObject("/base/joint/link1/joint/link2/joint")
        #self.joint4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint")
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4/p_e")

        self.pt_x = 1.1
        self.pt_y = 0.8
        self.pt_z = 0.4
        self.pt_theta = 0.0

        self.dp = 0.001

    def IK(self):

        sim = self.sim

        pos_of_pt = self.assign_pt_pos()
        pos_of_pe = self.get_pos_of_pe()
        #direction = self.decide_direction(pos_of_pe, pos_of_pt)

        print(f"pos_of_pe : {pos_of_pe}")
        print(f"pos of pt : {pos_of_pt}")


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
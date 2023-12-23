from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

class IK_XZ:

    def __init__(self, sim):

        #self.client = RemoteAPIClient()
        #client = self.client
        #self.sim = client.require('sim')
        #sim = self.sim

        self.sim = sim
        sim = self.sim

        # モデルの情報を取得
        self.base = sim.getObject("/base")
        self.joint1 = sim.getObject("/base/joint")
        self.link1 = sim.getObject("/base/joint/link1")
        self.joint2 = sim.getObject("/base/joint/link1/joint")
        self.link2 = sim.getObject("/base/joint/link1/joint/link2")
        self.joint3 = sim.getObject("/base/joint/link1/joint/link2/joint")
        self.link3 = sim.getObject("/base/joint/link1/joint/link2/joint/link3")
        self.joint4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint")
        self.link4 = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4")
        self.p_e = sim.getObject("/base/joint/link1/joint/link2/joint/link3/joint/link4/p_e")
        self.p_t = sim.getObject("/p_t")

        self.pt_x = 1.1
        self.pt_y = 0.4
        self.pt_z = 0.4
        self.pt_theta = 0.0

        self.dp = 0.001

        self.l1 = 0.4
        self.l2 = 0.5
        self.l3 = 0.5
        self.l4 = 0.2
        self.pt_theta = 0

    def IK(self):

        sim = self.sim
        sim.setStepping(True)
        sim.startSimulation()

        pos_pf_pt = self.assign_pt()

        #yakobi = self.calc_yakobi()

        #print(f"yakobi : {yakobi}")



    def assign_pt(self):

        pos_of_pt = np.empty(3)
        pos_of_pt[0] = self.pt_x
        pos_of_pt[1] = self.pt_z
        pos_of_pt[2] = self.pt_theta

        return pos_of_pt
    
    
    def calc_yakobi(self):

        sim = self.sim

        theta = self.get_joint_position()

        l2, l3, l4, j2, j3, j4 = sp.symbols("l2 l3 l4 j2 j3 j4")
        xe = l2 * sp.cos(j2) + l3 * sp.cos(j2 + j3) + l4 * sp.cos(j2 + j3 + j4)
        ye = l2 * sp.sin(j2) + l3 * sp.sin(j2 + j3) + l4 * sp.cos(j2 + j3 + j4)
        je = j2 + j3 + j4

        forward_pos = [xe, je, je]

        values_of_arm = {
            l2 : self.l2,
            l3 : self.l3,
            l4 : self.l4,
            j2 : theta[0],
            j3 : theta[1],
            j4 : theta[2]
        }

        yakobi = np.empty((0,3))

        for i in range(len(forward_pos)):

            j2_dot = sp.diff(forward_pos[i], j2)
            j2_dot = float(j2_dot.subs(values_of_arm))
            j3_dot = sp.diff(forward_pos[i], j3)
            j3_dot = float(j3_dot.subs(values_of_arm))
            j4_dot = sp.diff(forward_pos[i], j4)
            j4_dot = float(j4_dot.subs(values_of_arm))

            line = [j2_dot, j3_dot, j4_dot]
            yakobi = np.vstack((yakobi, line))
        
        return yakobi
    
    
    def get_joint_position(self):

        sim = self.sim

        theta = np.empty(3)

        theta[0] = sim.getJointPosition(self.joint2)
        theta[1] = sim.getJointPosition(self.joint3)
        theta[2] = sim.getJointPosition(self.joint4)

        return theta
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import sympy as sp

class IK_XZ:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
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
        self.pt_y = 0.8
        self.pt_z = 0.4
        self.pt_theta = 0.0

        self.dp = 0.001

    def IK(self):
        pass
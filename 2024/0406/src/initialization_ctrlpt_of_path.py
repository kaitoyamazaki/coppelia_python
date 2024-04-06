from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Setting:

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        self.start = sim.getObject("/start")
        self.dummy_size = 0.005
    
    def customize(self):

        sim = self.sim

        # 全ての角度を一定にするプログラムの作成
        #self.initialize()

        # 距離を一定距離にするプログラム
        self.ctrl_distance()
    

    def initialize(self):

        sim = self.sim

        path = sim.getObject("/Path")
        ctrlpt = sim.getObjectsInTree(path, sim.handle_all)

        theta = 40
        
        for i in range(6, len(ctrlpt)):
            #name = sim.getObjectAlias(ctrlpt[i], 1)
            #print(f"name : {name}")
            theta = theta * 1.045
            #print(f"theta : {theta}")
            ori = [0.0, 0.0, np.deg2rad(theta)]
            sim.setObjectOrientation(ctrlpt[i], ori, sim.handle_world)
    
    def ctrl_distance(self):
        
        sim = self.sim
        




def main():

    try:
        setting = Setting()
        setting.customize()
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")
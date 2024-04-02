# まず最初にstart地点から5本生やすところやる
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Path:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim

        self.start = sim.getObject('/start')
        self.dummy_size = 0.005
        self.distane = 0.03
        self.velocity = 0.001
        self.range_deg = [-20, -10, 0, 10, 20]
    
    def make_subtree(self):
        
        sim = self.sim
        pos = sim.getObjectPosition(self.start)
        ori = sim.getObjectOrientation(self.start)

        hoge = []

        for i in range(len(self.range_deg)):
            x = self.distance * np.sin(np.deg2rad(self.range_deg[i])) + pos[0]
            y = self.distance * np.cos(np.deg2rad(self.range_deg[i])) + pos[1]
            z = pos[2]

            point = [x, y, z]
            hoge.extend(point)
        
        reshape_hoge = [hoge[i:i+3] for i in range(0, len(hoge), 3)]

        for i in range(len(reshape_hoge)):
            point = sim.createDummy(self.dummy_size)
            sim.setObjectPosition(point, reshape_hoge[i], sim.handle_world)
            sim.setObjectOrientation(point, [0.0, 0.0, 0.0], sim.handle_world)

            sim.setObjectColor(point, 0, sim.colorcomponent_ambient_diffuse, [1.0, 0.0, 0.0])


    


def main():
    print(f'プログラム開始')
    path = Path()
    try:
        path.make_subtree()

    except KeyboardInterrupt:
        pass

    finally:
        print(f'プログラム終了')

if __name__ == '__main__':
    main()
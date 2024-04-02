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
        self.distance = 0.03
        self.velocity = 0.001
        self.range_deg = [-40, -20, 0, 20, 40]
    
    def make_subtree(self, sim):
        
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
            point_name = f'point{i}' 
            sim.setObjectAlias(point, point_name)
            sim.setObjectPosition(point, reshape_hoge[i], sim.handle_world)
            sim.setObjectOrientation(point, [0.0, 0.0, 0.0], sim.handle_world)

            sim.setObjectColor(point, 0, sim.colorcomponent_ambient_diffuse, [1.0, 0.0, 0.0])
        
    def check_subtree(self, sim):

        wrench = []

        for i in range(len(self.range_deg)):
            velocity = self.derive_velocity(sim, i)
            #wrench = self.derive_wrench()

            #self.check_wrench_point(wrench)


    def derive_velocity(self, sim, i):

        p0 = sim.getObjectPosition(self.start, sim.handle_world)
        

        point_name = f'/point{i}'
        point = sim.getObject(point_name)
        p1 = sim.getObjectPosition(point, sim.handle_world)
        print(f'p1 : {p1}')
            

def main():
    print(f'プログラム開始')
    path = Path()
    try:
        path.make_subtree(path.sim)
        path.check_subtree(path.sim)

    except KeyboardInterrupt:
        pass

    finally:
        print(f'プログラム終了')

if __name__ == '__main__':
    main()
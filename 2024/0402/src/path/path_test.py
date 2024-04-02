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

        for i in range(len(self.range_deg)):
            velocity = self.derive_velocity(sim, i)
            wrench = self.derive_wrench(sim, i, velocity)

            #self.check_wrench_point(wrench)


    def derive_velocity(self, sim, i):

        p0 = sim.getObjectPosition(self.start, sim.handle_world)

        point_name = f'/point{i}'
        point = sim.getObject(point_name)
        p1 = sim.getObjectPosition(point, sim.handle_world)

        real_deviation_of_x = p1[0] - p0[0]
        real_deviation_of_y = p1[1] - p0[1]
        real_deviation = [real_deviation_of_x, real_deviation_of_y]
        real_deviation_of_numpy = np.array(real_deviation)

        rate = 1 / 0.03
        deviation = rate * real_deviation_of_numpy
        
        return deviation

    
    def derive_wrench(self, sim, i, velocity):

        CoP = sim.getObject('/BaseRobot/CoP')
        CoG = sim.getObject('/target_object/cog')

        pos_of_CoP = sim.getObjectPosition(CoP, sim.handle_world)
        pos_of_CoG = sim.getObjectPosition(CoG, sim.handle_world)

        distance_x = pos_of_CoP[0] - pos_of_CoG[0]
        distance_y = pos_of_CoP[1] - pos_of_CoG[1]

        distance = [distance_x, distance_y]
        distance_numpy = np.array(distance)

        moment = np.cross(distance_numpy, velocity)
        moment = moment.tolist()

        wrench = [velocity[0], velocity[1], moment]

        return wrench

            

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
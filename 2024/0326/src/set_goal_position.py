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

        # ゴール地点を作成する関数, 必要に応じて実行
        #self.create_goal()

        # typeBに必要な円軌道のためのdummyを作成する関数
        self.create_circle_path()

    
    def create_goal(self):

        sim = self.sim
        goal = sim.createDummy(self.dummy_size)
        sim.setObjectAlias(goal, "goal")

        pos = sim.getObjectPosition(self.start, sim.handle_world)
        ori = sim.getObjectOrientation(self.start, sim.handle_world)

        pos[0] = pos[0] - 0.2
        ori[2] = ori[2] + np.deg2rad(180)

        sim.setObjectPosition(goal, pos, sim.handle_world)
        sim.setObjectOrientation(goal, ori, sim.handle_world)

        sim.setObjectColor(goal, 0, sim.colorcomponent_ambient_diffuse, [1.0, 0.0, 0.0])

    def create_circle_path(self):
        
        sim = self.sim
        goal = sim.getObject("/goal")
        first_pos = sim.getObjectPosition(goal, sim.handle_world)
        first_pos = [first_pos[0] + 0.1, first_pos[1], first_pos[2]]
        z = first_pos[2]
        num = 36
        dtheta = 180 / 36
        r = 0.1
        pose = []

        for i in range(num):
            x = r * np.cos(np.deg2rad(dtheta * i)) + first_pos[0]
            y = r * np.sin(np.deg2rad(dtheta * i)) + first_pos[1]
            point = [x, y, z, 0, 0, 0, 1]
            pose.extend(point)
            #test = sim.createDummy(self.dummy_size)
            #sim.setObjectPosition(test, point, sim.handle_world)
        
        #reshape_pose = pose.reshape(-1, 7)
        #print(pose)
        test_path = sim.createPath(pose, 0, 100, 1.0, 0, [0,0,1])


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
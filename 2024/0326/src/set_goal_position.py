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

        # ゴール地点を作成する関数, 必要に応じてコメント
        self.create_goal()
    
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
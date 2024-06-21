from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Setting:

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
    
    def customize(self):

        sim = self.sim

        self.check_distance(sim)


    def check_distance(self, sim):

        d1 = sim.getObject('/Path/ctrlPt')
        d2 = sim.getObject('/Path/ctrlPt1')

        p1 = sim.getObjectPosition(d1, sim.handle_world)
        p2 = sim.getObjectPosition(d2, sim.handle_world)

        p1 = np.array(p1)
        p2 = np.array(p2)

        distance = p2 - p1
        print(f'{distance}')
        distance = np.square(distance)
        Distance = np.sqrt(distance[0] + distance[1])
        #print(f'{Distance}')



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
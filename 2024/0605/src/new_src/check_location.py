from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

class Check:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim
    
    def check_location(self, sim):

        right_hand = sim.getObject('/BaseRobot/right_hand')
        left_hand = sim.getObject('/BaseRobot/left_hand')
        object = sim.getObject('/target_object/cog')

        right_pos = sim.getObjectPosition(right_hand, object)
        left_pos = sim.getObjectPosition(left_hand, object)

        right_pos = [round(pos, 3) for pos in right_pos]
        left_pos = [round(pos, 3) for pos in left_pos]

        #types = [type(data) for data in right_pos]

        #print(types)

        right_pos1 = right_pos
        right_pos2 = right_pos
        left_pos1 = left_pos

        print(f'right_hand : {right_pos}')
        print(f'left_hand : {left_pos}')
    

def main():

    try:
        check = Check()
        check.check_location(check.sim)
    
    except KeyboardInterrupt:
        print(f'Ctrl-Cによる終了')


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print(f'Ctrl-Cによる終了')
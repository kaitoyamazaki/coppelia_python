from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np
import pandas as pd
from time import sleep

class Path:

    def __init__(self):

        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim
    

    def get_contact_point_position(self, sim):

        contact_point1 = sim.getObject('/target_object/contact_point1')
        contact_point2 = sim.getObject('/target_object/contact_point2')
        contact_point3 = sim.getObject('/target_object/contact_point3')

        object_cog = sim.getObject('/target_object/')

        contact_point1_pos = sim.getObjectPosition(contact_point1, sim.handle_world)
        contact_point2_pos = sim.getObjectPosition(contact_point2, sim.handle_world)
        contact_point3_pos = sim.getObjectPosition(contact_point3, sim.handle_world)

        object_cog_pos = sim.getObjectPosition(object_cog, sim.handle_world)

        contact_point1_pos_numpy = np.array(contact_point1_pos)
        contact_point2_pos_numpy = np.array(contact_point2_pos)
        contact_point3_pos_numpy = np.array(contact_point3_pos)

        object_cog_pos_numpy = np.array(object_cog_pos)

        c_p_1 = contact_point1_pos_numpy - object_cog_pos
        c_p_2 = contact_point2_pos_numpy - object_cog_pos
        c_p_3 = contact_point3_pos_numpy - object_cog_pos

        c_p1_cog = [c_p_1[0]*1000, c_p_1[1]*1000]
        c_p2_cog = [c_p_2[0]*1000, c_p_2[1]*1000]
        c_p3_cog = [c_p_3[0]*1000, c_p_3[1]*1000]

        print(f'{c_p1_cog}, {c_p2_cog}, {c_p3_cog}')
        print(f'Successful operation!!!')


def main():
    print(f'プログラム開始')
    path = Path()
    try:
        path.get_contact_point_position(path.sim)

    except KeyboardInterrupt:
        pass

    finally:
        print(f'プログラム終了')

if __name__ == '__main__':
    main()
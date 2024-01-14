import math
import numpy as np

class MakingPath:

    def __init__(self):
        
        self.dt = 0.1
        self.acceleation = 1.06
        self.distance = 0.528
        self.target_veloccity = 0.106
        self.t_f = 5.1

        self.x0 = 0.0
        self.y0 = 0.0
    
    def control(self):

        t = 0
        velocity = 0
        acceleation = self.acceleation
        distance = self.distance
        dt = self.dt

        x = 0
        y = 0

        position = 0
        position1 = 0
        position2 = 0
        position3 = 0

        velocity1 = 0
        velocity2 = 0
        velocity3 = 0

        print(f"t, velocity, position")

        for t in np.arange(0.0, self.t_f+0.1, 0.1):
            print({t})


def main():

    try:
        making_path = MakingPath()
        making_path.control()
    
    except KeyboardInterrupt:
        print(f"Ctlr-Cによる終了")


if __name__ == "__main__":

    try:
        main()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")
import math
import numpy as np

class TrapezoidalControl:

    def __init__(self):
        
        self.dt = 0.1
        self.acceleration = 0.0085
        self.distance = 0.15
        self.target_velocity = 0.017
        self.t_f = 12.0

        self.y0 = 0.1274

    def control(self):

        t = 0
        velocity = 0
        acceleration = self.acceleration
        distance = self.distance
        y = self.y0

        position = 0
        position1 = 0
        position2 = 0
        position3 = 0

        velocity1 = 0
        velocity2 = 0
        velocity3 = 0

        dt = self.dt

        print(f"t, velocity, position")

        for t in np.arange(0.0, 12.1, 0.1):

            if(t <= 2.0):
                velocity2 = 0
                velocity3 = 0
                velocity1 = acceleration * t
                position1 = velocity1 * t / 2
            
            elif(t > 2.0 and t <= 10.0):
                velocity1 = 0
                velocity3 = 0
                velocity2 = self.target_velocity
                position2 = velocity2 * (t - 2.0)
            
            elif(t > 10.0):
                velocity1 = 0
                velocity2 = 0
                velocity3 = -acceleration * (t - 10.0) + self.target_velocity
                position3 = (self.target_velocity + velocity3) * (t - 10.0) / 2
            
            velocity = velocity1 + velocity2 + velocity3
            position = position1 + position2 + position3
            hand_position = self.y0 - position

            print(f"{t}, {velocity}, {hand_position}")
            






def main():

    try:
        control = TrapezoidalControl()
        control.control()

    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")
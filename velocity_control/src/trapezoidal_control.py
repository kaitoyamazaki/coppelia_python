import math
import numpy as np

class TrapezoidalControl:

    def __init__(self):
        
        self.dt = 0.1
        self.acceleration = 0.12
        self.distance = 0.3
        self.target_velocity = 0.06
        self.t_f = 5.5

        self.z0 = 0.4281

    def control(self):

        t = 0
        velocity = 0
        acceleration = self.acceleration
        distance = self.distance
        z = self.z0

        position = 0
        position1 = 0
        position2 = 0
        position3 = 0

        velocity1 = 0
        velocity2 = 0
        velocity3 = 0

        dt = self.dt

        print(f"t, velocity, position")

        for t in np.arange(0.0, 5.6, 0.1):

            if(t <= 0.5):
                velocity2 = 0
                velocity3 = 0
                velocity1 = acceleration * t
                position1 = velocity1 * t
            
            elif(t > 0.5 and t <= 5.0):
                velocity1 = 0
                velocity3 = 0
                velocity2 = self.target_velocity
                position2 = velocity2 * t
            
            elif(t > 5.0):
                velocity1 = 0
                velocity2 = 0
                velocity3 = -acceleration * (t - 5.0) + 0.06 
                position3 = (self.target_velocity + velocity3) * (t - 5.0) / 2
            
            velocity = velocity1 + velocity2 + velocity3
            position = position1 + position2 + position3
            hand_position = self.z0 - position

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
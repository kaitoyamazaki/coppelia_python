import math
import numpy as np

class TrapezoidalControl:

    def __init__(self):
        
        self.dt = 0.1
        self.acceleration = 0.3375
        self.distance = 0.130
        self.target_velocity = 0.03375
        self.t_f = 4.2

        #self.y0 = 0.11809
        self.y0 = 0.26709

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

        for t in np.arange(0.0, self.t_f, 0.1):

            if(t <= 0.1):
                velocity2 = 0
                velocity3 = 0
                velocity1 = acceleration * t
                position1 = velocity1 * t / 2
            
            elif(t > 0.1 and t <= 4.0):
                velocity1 = 0
                velocity3 = 0
                velocity2 = self.target_velocity
                position2 = velocity2 * (t - 0.1)
            
            elif(t > 4.0):
                velocity1 = 0
                velocity2 = 0
                velocity3 = -acceleration * (t - 4.0) + self.target_velocity
                position3 = (self.target_velocity + velocity3) * (t - 4.0) / 2
            
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
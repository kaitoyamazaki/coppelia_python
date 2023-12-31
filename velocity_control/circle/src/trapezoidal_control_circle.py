import math
import numpy as np

class TrapezoidalControl:

    def __init__(self):
        
        self.dt = 0.01
        self.distance = 0.408
        self.t_f = 5.11

        self.ddx = 0.816
        self.target_dx = 0.0816

        self.ddtheta = 720.0
        self.target_dtheta = 72.0

        self.x0 = 0
        self.y0 = 0.1365
        self.theta0 = 0


    def control(self):

        t = 0
        ddx = self.ddx
        ddtheta = self.ddtheta
        dt = self.dt
        
        x = self.x0
        y = self.y0
        theta = self.theta0

        theta1 = 0
        theta2 = 0
        theta3 = 0

        omega1 = 0
        omega2 = 0
        omega3 = 0
        
        v1 = 0
        v2 = 0
        v3 = 0

        x1 = 0
        x2 = 0
        x3 = 0

        vx1 = 0
        vx2 = 0
        vx3 = 0

        y1 = 0
        y2 = 0
        y3 = 0

        vy1 = 0
        vy2 = 0
        vy3 = 0

        #print(f"t, v, vx, vy, omega, x, y, theta")

        for t in np.arange(0.0, self.t_f, 0.01):

            if(t <= 0.1):
                omega2 = 0
                omega3 = 0

                omega1 = ddtheta * t
                theta1 = omega1 * t / 2


            
            elif(t > 0.1 and t <= 5.0):
                omega1 = 0
                omega3 = 0

                omega2 = self.target_dtheta
                theta2 = omega2 * (t - 0.1)
            
            elif(t > 5.0):
                omega1 = 0
                omega2 = 0

                omega3 = -ddtheta * (t - 5.0)
                theta3 = (self.target_dtheta + omega3) * (t - 5.0) / 2

            omega = omega1 + omega2 + omega3
            theta = theta1 + theta2 + theta3

            if(t <= 0.1):
                v2 = 0
                v3 = 0

                vx2 = 0
                vx3 = 0

                vy2 = 0
                vy3 = 0
                
                v1 = ddx * t
                vx1 = v1 * np.cos(np.deg2rad(theta))
                vy1 = v1 * np.sin(np.deg2rad(theta))

                x1 = vx1 * t / 2
                y1 = vy1 * t / 2
                
            elif(t > 0.1 and t <= 5.0):
                v1 = 0
                v3 = 0

                vx1 = 0
                vx3 = 0

                vy1 = 0
                vy3 = 0

                v2 =  self.target_dx
                vx2 = v2 * np.cos(np.deg2rad(theta))
                vy2 = v2 * np.sin(np.deg2rad(theta))

                x2 = vx2 * (t - 0.1)
                y2 = vy2 * (t - 0.1)

            elif(t > 5.0):
                v1 = 0
                v2 = 0

                vx1 = 0
                vx2 = 0

                vy1 = 0
                vy2 = 0

                v3 =  -ddx * (t - 5.0)
                vx3 = v3 * np.cos(np.deg2rad(theta))
                vy3 = v3 * np.sin(np.deg2rad(theta))

                x3 = vx3 * (t - 5.0)
                y3 = vy3 * (t - 5.0)

            vx = vx1 + vx2 + vx3
            vy = vy1 + vy2 + vy3

            x = x1 + x2 + x3 + self.x0
            y = y1 + y2 + y3 + self.y0

            print(f"{t}, {theta}, {vx}, {vy}, {x}, {y}")

            

            

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
import numpy as np

class TrapezoidalControl:

    def __init__(self):
        
        self.dt = 0.05
        self.distance = 0.408
        self.t_f = 5.15

        self.ddx = 0.816
        self.target_dx = 0.0816

        self.ddtheta = 720.0
        self.target_dtheta = 72.0

        self.x0 = 0.167
        self.y0 = -0.013
        self.theta0 = -90

        self.center_x = 0.167
        self.center_y = 0.061
        self.circle_r = 0.065

        self.base_x = 0.06638
        self.base_y = 0.20149

        self.base_x = 0.0
        self.base_y = 0.0

    def control(self):

        t = 0
        ddx = self.ddx
        ddtheta = self.ddtheta
        dt = self.dt
        
        x = self.x0
        y = self.y0
        theta = self.theta0

        center_x = self.center_x
        center_y = self.center_y

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

        print(f"t, omega, theta, x, y")

        for t in np.arange(0.0, self.t_f, dt):

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

                omega3 = -ddtheta * (t - 5.0) + self.target_dtheta
                theta3 = (self.target_dtheta + omega3) * (t - 5.0) / 2

            omega = omega1 + omega2 + omega3
            theta = theta1 + theta2 + theta3 + self.theta0

            x = self.circle_r * np.cos(np.deg2rad(theta)) + center_x
            y = self.circle_r * np.sin(np.deg2rad(theta)) + center_y

            print(f"{t}, {omega}, {theta}, {x}, {y}")

            

            

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
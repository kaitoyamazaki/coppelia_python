from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np


class Trace():

    def __init__(self):
        self.client = RemoteAPIClient()
        client = self.client
        self.sim = client.require('sim')
        sim = self.sim
        self.motor_r = sim.getObject('/base/right_motor')
        self.motor_l = sim.getObject('/base/left_motor')
        self.robot = sim.getObject('/base')
        self.middleSensor = sim.getObject('/base/middleSensor')
        self.rightSensor = sim.getObject('/base/rightSensor')
        self.leftSensor = sim.getObject('/base/leftSensor')
        
    
    def test(self):
        sim = self.sim
        test_pos = sim.getObjectPosition(self.robot, sim.handle_world)
        print(f"pos of robot is {test_pos}")

    def simulation(self):
        sim = self.sim
        sim.setStepping(True)

        sim.startSimulation()



        while (t := sim.getSimulationTime()) < 10:
            # typeエラーが出るのでその対策
            #try:
                #data_middle = middle[1][11]
                #data_right = right[1][11]
                #data_left = left[1][11]
                #print(f"{data_left, data_middle, data_right}")
            
            #except TypeError:
                #sim.step()
                #continue

            sim.step()
        sim.stopSimulation()



#def sys_init():
    #motor_r = sim.getObject('/base/right_motor')
    #motor_l = sim.getObject('/base/left_motor')
    #robot = sim.getObject('/')

    #return motor_r, motor_l

#def get_robot_pos():
    #robot = sim.getObject('/base')
    #robot_pos = sim.getObjectPosition(robot, sim.handle_world)

    #return robot_pos

#def line_sensor():
    #middle = sim.getObject('/base/middleSensor')
    #right = sim.getObject('/base/rightSensor')
    #left = sim.getObject('/base/leftSensor')

    #res_middle =  sim.readVisionSensor(middle)
    #res_right =  sim.readVisionSensor(right)
    #res_left =  sim.readVisionSensor(left)

    #return res_middle, res_right, res_left

#client = RemoteAPIClient()
#sim = client.require('sim')


#sim.setStepping(True)

#sim.startSimulation()



#while (t := sim.getSimulationTime()) < 10:
    ##print(f'Simulation time: {t:.2f} [s]')
    #robot_pos = get_robot_pos()
    #middle, right, left = line_sensor()
    
    ##print(f'robot positions: {np.round(robot_pos,3)} [m]')

    ## typeエラーが出るのでその対策
    #try:
        #data_middle = middle[1][11]
        #data_right = right[1][11]
        #data_left = left[1][11]
        #print(f"{data_left, data_middle, data_right}")
    
    #except TypeError:
        #sim.step()
        #continue

    #sim.step()
#sim.stopSimulation()

def main():
    trace = Trace()
    trace.simulation()



if __name__ == '__main__':
    main()
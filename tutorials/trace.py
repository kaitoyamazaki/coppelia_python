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
        #self.middleSensor = sim.getObject('/base/middleSensor')
        #self.rightSensor = sim.getObject('/base/rightSensor')
        #self.leftSensor = sim.getObject('/base/leftSensor')

    def linesensor(self):
        sim = self.sim
        sensor_value = np.empty(5)
        for i in range(5):
            sensor_name = "/base/" + str(i)
            now_sensor = sim.getObject(sensor_name)
            now_data = self.get_sensor_data(now_sensor)
            if (now_data < 0.1):
                sensor_value[i] = True
            
            else:
                sensor_value[i] = False
            #print(f"{i}番目のデータ : {now_data}")

        return sensor_value 
    
    def get_sensor_data(self, sensor):
        sim = self.sim
        result = sim.readVisionSensor(sensor)

        try:
            sensor_data = result[1][11]
        
        except TypeError:
            sensor_data = 100
            pass

        return sensor_data
        


    def simulation(self):
        sim = self.sim
        sim.setStepping(True)

        sim.startSimulation()

        while (t := sim.getSimulationTime()) < 10:

            now_sensor_data = self.linesensor()

            print(f"{now_sensor_data}")

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


def main():
    trace = Trace()
    trace.simulation()



if __name__ == '__main__':
    main()
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
        self.base_vel_r = sim.getJointTargetVelocity(self.motor_r)
        self.base_vel_l = sim.getJointTargetVelocity(self.motor_l)
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
    

    def motor_controll(self, sensora_data):
        sim = self.sim
        sensor_pos = [10, 5, 0, -5, -10]
        sum = 0
        ave = 0
        gain = 400

        vel_r = self.base_vel_r
        vel_l = self.base_vel_l

        for i in range(len(sensora_data)):
            if(sensora_data[i]):
                sum += 1
                ave += sensor_pos[i]
            
            else:
                pass
        

        try:
            now_pos = ave / sum

        except ZeroDivisionError:
            now_pos = 0
            vel_r = self.base_vel_r
            vel_l = self.base_vel_l
        

        out = now_pos * gain
        rad_out = np.deg2rad(out)

        vel_r = self.base_vel_r + rad_out
        vel_l = self.base_vel_l - rad_out

        print(f"{sensora_data}")
        print(f"{out}, {rad_out}")
        print(f"{vel_r}, {vel_l}")

        sim.setJointTargetVelocity(self.motor_r, vel_r)
        sim.setJointTargetVelocity(self.motor_l, vel_l)



        


    def simulation(self):
        sim = self.sim
        sim.setStepping(True)

        sim.startSimulation()

        while (t := sim.getSimulationTime()) < 100:

            now_sensor_data = self.linesensor()
            self.motor_controll(now_sensor_data)


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
    
    try:
        main()
    
    except KeyboardInterrupt:
        print((f"Ctrl-Cによるプログラム停止"))
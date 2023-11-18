from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.require('sim')

motor_r = sim.getObject('/o_robot/joint_r')
motor_l = sim.getObject('/o_robot/joint_l')

IMU = sim.getObject('/o_robot/IMU')



sim.setStepping(True)

sim.startSimulation()
while (t := sim.getSimulationTime()) < 30:
    #now_time = t * 0.05
    #position = sim.getObjectPosition(object, sim.handle_world)
    #position[0] = now_time
    #sim.setObjectPosition(object, position, sim.handle_world)
    #print(f"now position is {position}")
    #print(f'Simulation time: {t:.2f} [s]')

    IMU_ang = sim.getObjectOrientation(IMU, sim.handle_world)
    print(f"IMU_ang is {np.rad2deg(IMU_ang)}")

    #now_speed = sim.getJointVelocity(motor_r)
    #print(f"now speed is {now_speed}")
    sim.step()
sim.stopSimulation()
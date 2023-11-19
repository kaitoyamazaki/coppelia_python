from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

def __init__(sim):
    motor_r = sim.getObject('/o_robot/joint_r')
    motor_l = sim.getObject('/o_robot/joint_l')
    IMU = sim.getObject('/o_robot/IMU')
    target_ang = 0
    return motor_r, motor_l, IMU, target_ang

def main():
    client = RemoteAPIClient()
    sim = client.require('sim')
    target = -45
    motor_r, motor_l, IMU, target_ang = __init__(sim)
    sim.setStepping(True)
    sim.startSimulation()
    sim.setJointTargetPosition(motor_r, np.deg2rad(target))
    sim.setJointTargetPosition(motor_l, np.deg2rad(target))
    while (t := sim.getSimulationTime()) < 10:
        #IMU_ang = sim.getObjectOrientation(IMU, sim.handle_world)
        #diff_ang = target_ang - IMU_ang[0]
        #diff_ang = np.rad2deg(diff_ang)
        # 振動の様子も見たいので若干数値を加算する
        #diff_ang = diff_ang
        #sim.setJointTargetPosition(motor_r, -diff_ang)
        #sim.setJointTargetPosition(motor_l, -diff_ang)
        #now_target_position_r = sim.getJointTargetPosition(motor_r)
        #now_target_position_l = sim.getJointTargetPosition(motor_l)
        #print(f"currently target angle, right motor : {np.rad2deg(now_target_position_r)}, left motor : {np.rad2deg(now_target_position_l)}")
        sim.step()
    sim.stopSimulation()

if __name__ == '__main__':
    main()
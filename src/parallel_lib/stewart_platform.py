import numpy as np
from parallel_lib import utilities as util
from parallel_lib import parallel_robot as prl

def distribute_angles(theta):
    onetwentydegrees = 2 * np.pi / 3
    angles = [
        theta,
        onetwentydegrees - theta,
        onetwentydegrees + theta,
        2 * onetwentydegrees - theta,
        2 * onetwentydegrees + theta,
        3 * onetwentydegrees - theta,
    ]
    return angles

class StewartPlatform(prl.ParallelRobot):
    def __init__(self, rbase: float, thetabase: float, rend: float, thetaend: float):
        '''
        This code creates a circle to represent the base and then use different angles to get
        the 3D coordinates for the 6 points we will use for the joints. This works for both
        the base and the end effector. Thetabase and thetaend are both in radians.
        '''
        base_angles = distribute_angles(thetabase)
        end_angles = distribute_angles(thetaend + 60)
        joints = []
        for joint_no in range(6):
            joints.append((
                [rbase * np.cos(base_angles[joint_no]), rbase * np.sin(base_angles[joint_no]), 0], 
                [rbase * np.cos(end_angles[joint_no]), rbase * np.sin(end_angles[joint_no]), 0],
            ))
        super().__init__(joints)
    def len_to_pose(self,joints:list,length:list,height:int):

        if index is None:
            index = self.n
        assert 0 <= index <= self.n, "Invalid index value!"
        Answer = np.zeros(6,self.n)
        z_limit = max(length)
        end_cord = [0,0,0,0,0]
        for i in range(index):
            joint_a = joints[i,0]
            joint_b = joints[i,1]
            joint_b_x = joint_b[0]+end_cord[0]+sin()

        


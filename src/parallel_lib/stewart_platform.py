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
        base_angles = distribute_angles(thetabase)
        end_angels = distribute_angles(thetaend)
        

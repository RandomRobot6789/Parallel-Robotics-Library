import parallel_lib.stewart_platform as stew
import parallel_lib.utilities
import parallel_lib.visualization as viz
import numpy as np


robot = stew.StewartPlatform(2, np.pi / 12, 1, np.pi / 12)


T = parallel_lib.utilities.se3(parallel_lib.utilities.roty(np.pi / 12), np.array([1, 0, 2]))

viz.show(robot, T)
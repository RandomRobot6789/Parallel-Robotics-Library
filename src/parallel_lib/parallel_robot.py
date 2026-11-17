import numpy as np
from numpy.typing import NDArray
from typing import Callable, Iterable

class ParallelRobot:
    def __init__(self, actuators: list[list[list[float]]]):
        """
        bot = ParallelRobot(cables)

        Creates an instance of a parallel robot. Assumes prismatic joints, not rotary ones.

        :param list[list[float]] cables: n length list where each entry is a tuple of two 3-vectors in homogenous representation.
        The first vector is the actuator mounting point in the base frame, while the second is the actuator mounting point
        in the manipulator frame
        """
        self.n = len(actuators)
        self.actuators = actuators

    def forward_kinematics(self, lengths: list[float]) -> NDArray:
        """
        T_end = bot.forward_kinematics(lengths)

        Returns the transform from the base frame to the end frame given a set of
        actuator lengths.

        :param list[float] lengths: list or iterable of floats which represent the actuator lengths.

        :return T: the 4 x 4 homogeneous transform between the specified frames.
        """

        return

    def inverse_kinematics(self, T: NDArray) -> list[float]:
        """
        length_list = bot.inverse_kinematics(T)

        Returns the actuator lengths given the transform from the base to end frames.
        :param NDArray T: SO(3) transformation to the end frame.

        :return list[float] lengths: list of floats which represent the actuator lengths.
        """
        lengths = []
        def length(vector: NDArray):
            return np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
        for joint_no in range(self.n):
            base_vector = self.actuators[joint_no][0]
            end_vector = T @ self.actuators[joint_no][1]
            lengths.append(length(end_vector - base_vector))
        return lengths
import numpy as np
from numpy.typing import NDArray
from typing import Callable, Iterable

class ParallelRobot:
    def __init__(self, actuators: list[list[float]]):
        """
        bot = ParallelRobot(cables)

        :param list[list[float]] cables: n length list where each entry is a tuple of two 3-vectors.
        The first vector is the actuator mounting point in the base frame, while the second is the actuator mounting point
        in the manipulator frame
        """
        self.n = len(actuators)
        self.cables = actuators

    def forward_kinematics(self, lengths: list[float]) -> NDArray:
        """
        T_end = bot.forward_kinematics(lengths)

        Returns the transform from the base frame to the end frame given a set of
        actuator lengths.

        :param list[float] lengths: list or iterable of floats which represent the joint angles.

        :return T: the 4 x 4 homogeneous transform between the specified frames.
        """

        return

    def inverse_kinematics(self, T: NDArray) -> list[float]:
        """
        length_list = bot.inverse_kinematics(T)

        Returns the actuator lengths given the transform from the base to end frames.
        :param NDArray T: SO(3) transformation to the end frame.

        :return T: the 4 x 4 homogeneous transform between the specified frames.
        """
        return
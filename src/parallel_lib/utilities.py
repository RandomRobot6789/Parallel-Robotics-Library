"""
Contains code to describe SO(3) and SE(3)

Copied from HW 04, "transforms.py".
"""

import numpy as np
from numpy import sin, cos, sqrt
from numpy.typing import NDArray

## 2D Rotations
def rot2(theta: float) -> NDArray:
    """
    R = rot2(th)

    :param float theta: angle of rotation (rad)
    :return R: 2x2 numpy array representing rotation in 2D by theta
    """
    # TODO: Implement the 2D SO(2) rotation matrix.
    # HW02 student task

    return np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])


## 3D Rotations
def rotx(theta: float) -> NDArray:
    """
    R = rotx(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about x-axis by amount theta
    """
    # TODO: Implement the 3D rotation matrix about the x-axis.
    # HW02 student task

    return np.array([[1, 0, 0], [0, cos(theta), -sin(theta)], [0, sin(theta), cos(theta)]])


def roty(theta: float) -> NDArray:
    """
    R = roty(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about y-axis by amount theta
    """
    # TODO: Implement the 3D rotation matrix about the y-axis.
    # HW02 student task

    return np.array([[cos(theta), 0, sin(theta)], [0, 1, 0], [-sin(theta), 0, cos(theta)]])


def rotz(theta: float) -> NDArray:
    """
    R = rotz(theta)

    :param float theta: angle of rotation (rad)
    :return R: 3x3 numpy array representing rotation about z-axis by amount theta
    """
    # TODO: Implement the 3D rotation matrix about the z-axis.
    # HW02 student task

    return np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])


# inverse of rotation matrix
def rot_inv(R: NDArray) -> NDArray:
    """
    R_inv = rot_inv(R)

    :param NDArray R: 2x2 or 3x3 numpy array representing a proper rotation matrix
    :return R_inv: 2x2 or 3x3 inverse of the input rotation matrix
    """
    # : Implement matrix inversion for SO(2) and SO(3).
    # HW02 student task

    return R.transpose()

def se3(R: NDArray = np.eye(3), p: NDArray = np.zeros(3)) -> NDArray:
    """
    T = se3(R, p)

    Creates a 4x4 homogeneous transformation matrix "T" from a 3x3 rotation matrix
    and a position vector.

    :param NDArray R: 3x3 numpy array representing orientation, defaults to identity.
    :param NDArray p: numpy array representing position, defaults to [0, 0, 0].
    :return T: 4x4 numpy array representing the homogeneous transform.
    """

    # : Construct a 4x4 homogeneous transform from a rotation matrix and translation vector.
    # HW03 student task

    return np.concat([np.concat([R, np.array([p]).T], axis=1), np.array([[0, 0, 0, 1]])])


def inv(T: NDArray) -> NDArray:
    """
    T_inv = inv(T)

    Returns the inverse transform to T.

    :param NDArray T: 4x4 homogeneous transformation matrix
    :return T_inv: 4x4 numpy array that is the inverse to T so that T @ T_inv = I
    """

    # TODO: Implement the inverse of a 4x4 homogeneous transform.
    # HW03 student task

    R = T[:3, :3]
    p = T[:3, 3]
    return se3(R.T, R.T @ (-p))


def R2rpy(R: NDArray) -> NDArray:
    """
    rpy = R2rpy(R)

    Returns the roll-pitch-yaw representation of the SO3 rotation matrix.

    :param NDArray R: 3x3 Numpy array for any rotation.
    :return rpy: Numpy array, containing [roll, pitch, yaw] coordinates (in radians).
    """

    # Implement conversion from a rotation matrix to roll-pitch-yaw angles.
    # HW04 student task

    return np.array([np.atan2(R[1, 0], R[0, 0]), np.atan2(-R[2, 0], np.sqrt(R[2, 1]**2 + R[2, 2]**2)), np.atan2(R[2, 1], R[2, 2])])


def R2axis(R: NDArray) -> NDArray:
    """
    axis_angle = R2axis(R)

    Returns an axis angle representation of a SO(3) rotation matrix.

    :param NDArray R: 3x3 rotation matrix.
    :return axis_angle: numpy array containing the axis angle representation
        in the form: [angle, rx, ry, rz]
    """

    # see equation (2.27) and (2.28) on pg. 54, using functions like "np.acos," "np.sin," etc.

    # Implement conversion from a rotation matrix to axis-angle form.
    # HW04 student task

    theta = np.acos((R[0,0] + R[1,1] + R[2,2] - 1) / 2)

    return np.array([theta, (R[2,1] - R[1,2]) / (2 * np.sin(theta)), (R[0,2] - R[2,0]) / (2 * np.sin(theta)), (R[1,0] - R[0,1]) / (2 * np.sin(theta))])


def axis2R(angle: float, axis: NDArray) -> NDArray:
    """
    R = axis2R(angle, axis)

    Returns an SO3 object of the rotation specified by the axis-angle.

    :param float angle: the angle to rotate about the axis (in radians).
    :param NDArray axis: components of the unit axis about which to rotate as
        a numpy array [rx, ry, rz].
    :return R: 3x3 numpy array representing the rotation matrix.
    """

    # follow formula in book, see equation (2.25) on pg. 54
    # Implement conversion from axis-angle form to a rotation matrix.
    # HW04 student task

    x, y, z = axis[0], axis[1], axis[2]
    c, s = np.cos(angle), np.sin(angle)
    return np.array([
        [x**2 * (1 - c) + c, x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
        [x * y * (1 - c) + z * s, y**2 * (1 - c) + c, y * z * (1 - c) - x * s],
        [x * z * (1 - c) - y * s, y * z * (1 - c) + x * s, z**2 * (1 - c) + c]
    ])


def R2quat(R: NDArray) -> NDArray:
    """
    quaternion = R2quat(R)

    Returns a quaternion representation of pose.

    :param NDArray R: 3x3 rotation matrix.
    :return quaternion: numpy array for the quaternion representation of pose in
        the format [nu, ex, ey, ez]
    """

    # Implement conversion from a rotation matrix to quaternion form.
    # HW04 student task

    angle, x, y, z = R2axis(R)
    nu = np.cos(angle / 2)
    ex, ey, ez = [np.sin(angle / 2) * r for r in (x, y, z)]
    return np.array([nu, ex, ey, ez])


def quat2R(q: NDArray) -> NDArray:
    """
    R = quat2R(q)

    Returns a 3x3 rotation matrix from a quaternion.

    :param NDArray q: [nu, ex, ey, ez ] - defining the quaternion.
    :return R: numpy array, 3x3 rotation matrix.
    """

    # Implement conversion from quaternion form to a rotation matrix.
    # HW04 student task

    nu, ex, ey, ez = q
    return np.array([
        [2 * (nu**2 + ex**2) - 1, 2 * (ex * ey - nu * ez), 2 * (ex * ez + nu * ey)],
        [2 * (ex * ey + nu * ez), 2 * (nu**2 + ey**2) - 1, 2 * (ey * ez - nu * ex)],
        [2 * (ex * ez - nu * ey), 2 * (ey * ez + nu * ex), 2 * (nu**2 + ez**2) - 1]
    ])


def euler2R(th1: float, th2: float, th3: float, order: str = "xyz") -> NDArray:
    """
    R = euler2R(th1, th2, th3, order='xyz')

    Returns a 3x3 rotation matrix as specified by the euler angles, we assume in all cases
    that these are defined about the "current axis," which is why there are only 12 versions
    (instead of the 24 possiblities noted in the course slides).

    :param float th1: angle of rotation about 1st axis (rad)
    :param float th2: angle of rotation about 2nd axis (rad)
    :param float th3: angle of rotation about 3rd axis (rad)
    :param str order: specifies the euler rotation to use, for example 'xyx', 'zyz', etc.
    :return R: 3x3 numpy array, the rotation matrix.
    """

    # Implement conversion from Euler angles to a rotation matrix.
    # HW04 student task

    def partialR(angle, char):
        if (char=="x"):
            return rotx(angle)
        if (char=="y"):
            return roty(angle)
        if (char=="z"):
            return rotz(angle)
        raise Exception("Bad angle value")

    R1, R2, R3 = partialR(th1, order[0]), partialR(th2, order[1]), partialR(th3, order[2])

    return R1@R2@R3


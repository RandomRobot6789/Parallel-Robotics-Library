import numpy as np
import pyvista as pv
from parallel_lib import parallel_robot


def show(robot: parallel_robot.ParallelRobot, T):

    base_vertices = np.array([robot.actuators[i][0][:3] for i in range(robot.n)])
    end_vertices = np.array([(T @ robot.actuators[i][1])[:3] for i in range(robot.n)])
    face = np.array([[6, 0, 1, 2, 3, 4, 5]])

    surface_base = pv.PolyData(base_vertices, face)
    surface_end = pv.PolyData(end_vertices, face)

    pl = pv.Plotter()
    pl.add_mesh(surface_base)
    pl.add_mesh(surface_end)

    for i in range(robot.n):   
        line = pv.Line(base_vertices[i], end_vertices[i])
        pl.add_mesh(line.tube(radius = 0.06), scalars = None, color='gray')

    pl.add_axes()
    pl.show()

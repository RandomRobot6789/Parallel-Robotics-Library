import numpy as np
import pyvista as pv

import parallel_lib.stewart_platform as stew
import parallel_lib.utilities

T = parallel_lib.utilities.se3(parallel_lib.utilities.roty(np.pi / 12), np.array([1, 0, 2]))

robot = stew.StewartPlatform(2, np.pi / 12, 1, np.pi / 12)

base_vertices = np.array([robot.actuators[i][0][:3] for i in range(robot.n)])
end_vertices = np.array([(T @ robot.actuators[i][1])[:3] for i in range(robot.n)])
face = np.array([[6, 0, 1, 2, 3, 4, 5]])

print(base_vertices)
surface_base = pv.PolyData(base_vertices, face)
surface_end = pv.PolyData(end_vertices, face)

pl = pv.Plotter()
pl.add_mesh(surface_base)
pl.add_mesh(surface_end)

for i in range(robot.n):   
    line = pv.Line(base_vertices[i], end_vertices[i])

    pl.add_mesh(line.tube(radius = 0.06))

pl.add_axes()
pl.show()

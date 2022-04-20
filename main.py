from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=1)
##scene.set_directional_light((1, 1, 1), 0.01, (1, 1, 1))
scene.set_background_color((0.0, 0.0, 0.0))
scene.set_floor(-0.94, (1.0, 1.0, 1.0))


@ti.kernel
def initialize_voxels():
    n = 60
    for i, j, k in ti.ndrange((-n, n), (-n, n), (-n, n)):
        x = float(i)/35
        y = float(j)/35
        z = float(k)/35
        x1 = float(i) / 38
        y1 = float(j) / 38
        z1 = float(k) / 38
        x2 = float(i) / 35
        y2 = float(j) / 35
        z2 = float(k) / 35
        x3 = float(i) / 45
        y3 = float(j) / 45
        z3 = float(k) / 45
        if (x*x + y*y - x*x * z + y*y * z + z*z - 1) < 0.1:
            scene.set_voxel(vec3(i, j, k), 1, vec3(0.9, 0.3, 0.3))
        if (((1/5)*(x1**2+y1**2+z1**2))**-6+((2)**-8*(x1**8+y1**8+z1**8))**6-1)<0:
            scene.set_voxel(vec3(i, j, k), 1.4, vec3(1, 1, 1))
            if (((1 / 5) * (x3 ** 2 + y3 ** 2 + z3 ** 2)) ** -6 + (
                    (2) ** -8 * (x3 ** 8 + y3 ** 8 + z3 ** 8)) ** 6 - 1) < 0:
                scene.set_voxel(vec3(i, j, k), 2, vec3(1, .9, .9))
        if (((1/5)*(x1**2+y1**2+z1**2))**-6+((2)**-8*(x1**8+y1**8+z1**8))**6-1)>0:
            if (((1 / 5) * (x2 ** 2 + y2 ** 2 + z2 ** 2)) ** -6 + (
                    (2) ** -8 * (x2 ** 8 + y2 ** 8 + z2 ** 8)) ** 6 - 1) < 0:
                scene.set_voxel(vec3(i, j, k), 2, vec3(1, 1, 1))



initialize_voxels()
scene.finish()


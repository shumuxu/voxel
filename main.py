from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=1)
##scene.set_directional_light((1, 1, 1), 0.01, (1, 1, 1))
scene.set_background_color((0.0, 0.0, 0.0))
scene.set_floor(-0.94, (1.0, 1.0, 1.0))


@ti.func
def shape1(x, y, z):
    return x * x + y * y - x * x * z + y * y * z + z * z - 1


@ti.func
def shape2(x, y, z):
    return ((1 / 5) * (x ** 2 + y ** 2 + z ** 2)) ** -6 + (2 ** -8 * (x ** 8 + y ** 8 + z ** 8)) ** 6 - 1


@ti.kernel
def initialize_voxels():
    n = 60
    num1 = 35
    num2 = 38
    num3 = 45
    for i, j, k in ti.ndrange((-n, n), (-n, n), (-n, n)):
        x = float(i) / num1
        y = float(j) / num1
        z = float(k) / num1
        x1 = float(i) / num2
        y1 = float(j) / num2
        z1 = float(k) / num2
        x3 = float(i) / num3
        y3 = float(j) / num3
        z3 = float(k) / num3
        if shape1(x, y, z) < 0.1:
            scene.set_voxel(vec3(i, j, k), 1, vec3(0.9, 0.3, 0.3))
        if shape2(x1, y1, z1) < 0:
            scene.set_voxel(vec3(i, j, k), 1.4, vec3(1, 1, 1))
            if shape2(x3, y3, z3) < 0:
                scene.set_voxel(vec3(i, j, k), 2, vec3(1, .9, .9))
        if shape2(x1, y1, z1) > 0:
            if shape2(x, y, z) < 0:
                scene.set_voxel(vec3(i, j, k), 2, vec3(1, 1, 1))


initialize_voxels()
scene.finish()


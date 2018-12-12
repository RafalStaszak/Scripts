import numpy as np
import numpy.linalg as lg
import random


def fibonacci_sphere(samples=1, randomize=True, dist=1):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    xs = []
    ys = []
    zs = []
    offset = 2. / samples
    increment = np.pi * (3. - np.sqrt(5.));

    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2);
        r = np.sqrt(1 - pow(y, 2))

        phi = ((i + rnd) % samples) * increment

        x = np.cos(phi) * r
        z = np.sin(phi) * r

        xs.append(dist * x)
        ys.append(dist * y)
        zs.append(dist * z)

    return np.stack(xs), np.stack(ys), np.stack(zs)


def generate_euler_angles():
    euler_angles = []
    angles_x = np.linspace(0,20*2*np.pi,60)
    angles_y = np.linspace(0, 2 * np.pi, 50)
    angles_z = np.linspace(np.deg2rad(-40), np.deg2rad(40), 10)
    for y in angles_y:
        for z in angles_z:
            for x in angles_x:
                euler_angles.append([x, y, z])

    return np.stack(euler_angles)




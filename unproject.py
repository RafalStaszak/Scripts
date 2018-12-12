import numpy as np
import math

eye_vec = np.array([0, 0, 0])
at_vec = np.array([0, 0, -1])
up_vec = np.array([0, 1, 0])
viewport = np.array([0, 0 , 800, 600])
coordinates = (np.array([10, 20 ,100, 0]))
near = 1
far = 100

def norm(vector):
    return vector/np.sqrt(np.sum(np.square(vector)))

def view_matrix(eye, at, up):
    z_axis = norm(eye-at)
    x_axis = norm(np.cross(up, z_axis))
    y_axis = np.cross(z_axis, x_axis)
    x_pos = np.dot(x_axis, eye)
    y_pos = np.dot(y_axis, eye)
    z_pos = np.dot(z_axis, eye)
    x = np.append(x_axis, x_pos)
    y = np.append(y_axis, y_pos)
    z = np.append(z_axis, z_pos)
    view = np.array([x, y, z, np.array([0, 0, 0, 1])])
    return np.transpose(view)

def projection_matrix(aspect_ratio, fov, near, far):
    projection = np.eye(4,4)
    projection[0][0] = 1/math.tan(fov/2)/aspect_ratio
    projection[1][1] = 1/math.tan(fov/2)
    projection[2][2] = far / (far - near)
    projection[2][3] = - 2 * far * near / (far - near)
    projection[3][2] = -1
    return projection


def unproject(win_x, win_y, win_z, view, projection, viewport):
    A = np.matmul(projection, view).astype(dtype=np.float32)
    M = np.linalg.inv(A)

    IN = np.empty((4))
    IN[0] = (win_x - viewport[0])/viewport[2]*2.0 - 1.0
    IN[1] = (win_y - viewport[1])/viewport[3]*2.0 - 1.0
    IN[2] = 2.0*win_z - 1.0

    OUT = np.matmul(M, IN)

    return  OUT[0]*OUT[3], OUT[1]*OUT[3], OUT[2]*OUT[3]



view = view_matrix(eye_vec, at_vec, up_vec)
projection = projection_matrix(800/600, math.radians(40.0), 1.0, 10.0)

print(unproject(0, 0, 10, view, projection, viewport))

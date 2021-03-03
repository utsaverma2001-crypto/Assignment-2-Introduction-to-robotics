import numpy as np
import math

coordinates = np.ones((4, 1))
coordinates[0] = float(input('Enter X coordinate: '))
coordinates[1] = float(input('Enter Y coordinate: '))
coordinates[2] = float(input('Enter Z coordinate: '))
ch = 'y'
while ch == 'y':
    axis = input('Enter axis for rotation: ')
    angle = float(input('Enter angle of rotation: '))
    rot = np.zeros((4, 4))
    rot[3][3] = 1
    if axis == 'x':
        rot[0][0] = 1;
        rot[1][1] = math.cos(math.radians(angle))
        rot[1][2] = -math.sin(math.radians(angle))
        rot[2][1] = math.sin(math.radians(angle))
        rot[2][2] = math.cos(math.radians(angle))
    if axis == 'y':
        rot[0][0] = math.cos(math.radians(angle))
        rot[0][2] = math.sin(math.radians(angle))
        rot[2][0] = -math.sin(math.radians(angle))
        rot[2][2] = math.cos(math.radians(angle))
        rot[1][1] = 1
    if axis == 'z':
        rot[0][0] = math.cos(math.radians(angle))
        rot[1][0] = math.sin(math.radians(angle))
        rot[0][1] = -math.sin(math.radians(angle))
        rot[1][1] = math.cos(math.radians(angle))
        rot[2][2] = 1
    rot[0][3] = float(input('Input translation for x axis(0 if none): '))
    rot[1][3] = float(input('Input translation for y axis(0 if none): '))
    rot[2][3] = float(input('Input translation for z axis(0 if none): '))
    ans = np.zeros((4, 1))
    for i in range(len(rot)):
        for j in range(len(coordinates[0])):
            for k in range(len(coordinates)):
                ans[i][j] += rot[i][k] * coordinates[k][j]
    coordinates = ans
    ch = input("Want to add another set of rotation and translation(y/n): ")

print('Coordinates with respect to  original frame are: ')
print('X: {}'.format(float(coordinates[0])))
print('Y: {}'.format(float(coordinates[1])))
print('Z: {}'.format(float(coordinates[2])))

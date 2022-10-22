import time
import board
import adafruit_mpu6050
from math import atan2, degrees, pi, sqrt
# from pykalman import KalmanFilter
import numpy as np
from numpy import diff



i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c,address= 0x68)


isCalibrated = False
prevSpeedMatrix = [0,0,0]
rotationMatrix = [0,0,0]

pos = np.zeros((1,3))


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def calcAngles(x,y,z):
    return vector_2_degrees(x, y), vector_2_degrees(x, z), vector_2_degrees(y, z)

def calibrate(timeCal): #how long calibration takes
    run = True
    global isCalibrated, rotationMatrix
    calibrating = False
    initT= time.time()
    while run:
        currT = time.time() - initT
        print(mpu.acceleration[2], calibrating)
        if not isCalibrated and not calibrating and 9 < mpu.acceleration[2] < 10 :
            calibrating = True
            initT= time.time()
        elif not 8.6 < mpu.acceleration[2] < 9.4:
            calibrating = False
        elif calibrating and currT > timeCal:
            isCalibrated = True
            calibrating = False
            run = False
            rotationMatrix = [0,0,0]
            print("done calibrating")


def stop(points):
    points = points[-11:-1]
    points = np.sqrt(np.sum(np.square(points), axis = 1))

    return
allAccel = np.zeros((20,3))

start = time.time()
while time.time() - start < 4:
    # if not isCalibrated:
    #     calibrate(3)
    accel = np.zeros(3)

    for i in range(10):
        newAccel = np.array(mpu.acceleration)
        accel = np.add(accel, newAccel) #m/s/s
    accel = accel/10
    accel = np.append(accel, (time.time() - start))
    print(accel[0],",",accel[1],",",accel[2],",", time.time() - start)
    # print(accel.shape)


    allAccel = np.append(allAccel, accel[np.newaxis,:],axis = 0)


dx = np.diff(allAccel[:,0])/allAccel[:,3]
dy = np.diff(allAccel[:,1])/allAccel[:,3]
dz = np.diff(allAccel[:,2])/allAccel[:,3]
print(dx,dy,dz,allAccel[:,3])










    # print(mpu.acceleration[0],mpu.acceleration[1],mpu.acceleration[2], mpu.gyro[0],mpu.gyro[1],mpu.gyro[2])

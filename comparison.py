import math
import numpy as np
import pandas as pd


#numpy array of ideal ## acceleration
ideal = np.array()
#numpy array of actual ## acceleration 
actual = np.array() ## gonna pretend this is already calibrated and holds distances

def get_euclidean(ideal, actual): # returns the euclidean distance of actual xyz pos and ideal xyz pos
    ideal = pd.DataFrame(ideal, columns = ['acc_x','acc_y','acc_z','gyr_x','gyr_y','gyr_z'])
    ideal_x = ideal.iloc[:, 0]
    ideal_y = ideal.iloc[: , :1]
    ideal_z = ideal.iloc[: , :2]

    actual = pd.DataFrame(actual, columns = ['acc_x','acc_y','acc_z','gyr_x','gyr_y','gyr_z'])
    actual_x = actual.iloc[:, 0]
    actual_y = actual.iloc[: , :1]
    actual_z = actual.iloc[: , :2]
   
   
    x_dist = [(a-b)*(a-b) for a, b in zip(ideal_x, actual_x)]
    y_dist = [(a-b)*(a-b) for a, b in zip(ideal_y, actual_x)]
    z_dist = [(a-b)*(a-b) for a, b in zip(ideal_z, actual_z)]
    
    dist = [math.sqrt(x**2 + y**2 + z**2) for x, y, z in zip(x_dist, y_dist, z_dist)]
    return dist

def mark_differences(ideal, actual, threshold): # returns a flag of what time series data were off and in which direction
    ideal = pd.DataFrame(ideal, columns = ['acc_x','acc_y','acc_z','gyr_x','gyr_y','gyr_z'])
    ideal_x = ideal.iloc[:, 0]
    ideal_y = ideal.iloc[: , :1]
    ideal_z = ideal.iloc[: , :2]

    actual = pd.DataFrame(actual, columns = ['acc_x','acc_y','acc_z','gyr_x','gyr_y','gyr_z'])
    actual_x = actual.iloc[:, 0]
    actual_y = actual.iloc[: , :1]
    actual_z = actual.iloc[: , :2]
   
   
    x_dist = [(a-b)*(a-b) for a, b in zip(ideal_x, actual_x)]
    y_dist = [(a-b)*(a-b) for a, b in zip(ideal_y, actual_x)]
    z_dist = [(a-b)*(a-b) for a, b in zip(ideal_z, actual_z)]
    
    dist = [math.sqrt(x**2 + y**2 + z**2) for x, y, z in zip(x_dist, y_dist, z_dist)]
    pass
    
get_euclidean(ideal, actual)

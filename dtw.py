import pandas as pd
import numpy as np
from matplotlib import pyplot as mp

one = pd.read_csv("test4.csv")
# two = pd.read_csv("slow.csv")
three = pd.read_csv("test1.csv")

trimmed_1 = one.iloc[:,0]
# trimmed_2 = two.iloc[:,0]
trimmed_3 = three.iloc[:,0]
# print(trimmed_1.to_numpy())
# print(trimmed_2.to_numpy())
# print(trimmed_3.to_numpy())

def dtw(s, t):
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            # take last min from a square box
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix

x = np.arange(len(trimmed_1))
mp.plot(one.iloc[:,3], one.iloc[:,0])
mp.plot(one.iloc[:,3], one.iloc[:,1])
mp.plot(one.iloc[:,3], one.iloc[:,2])
mp.savefig("graph.png")
#test = dtw(trimmed_1.to_numpy(), trimmed_2.to_numpy())
#print(test[-1][-1])


#test = dtw(trimmed_2.to_numpy(), trimmed_3.to_numpy())
# print(test[-1][-1])



test = dtw(trimmed_1.to_numpy(), trimmed_3.to_numpy())
print(test[-1][-1])



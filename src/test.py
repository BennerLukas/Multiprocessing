import numpy as np 
import time
import math
from multiprocessing import Pool
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sbn 




def create_points(dimension=3, n=1000000):
    'creates 3D Points'
    points = 10* np.random.rand(n,dimension)
    return points

def calc_distance(x1, x2):
    'calculate distance between 2 Points'
    distance = np.linalg.norm(x1-x2)
    return distance

def calc_distance_classic(x1,x2):
    distance=0
    for i in range(len(x1)):
        distance += (x1[i] - x2[i] )**2
    return math.sqrt(distance)

def get_distances_multi(x1, points,pool=15):
    'calculate distance to every other point with mutliprocessing'
    distances = []
    t2 = time.time()
    if __name__ == '__main__':
        with Pool(pool) as p:
            distance = p.starmap(calc_distance,[(x1,p) for p in points])
            distances.append(distance)
    #print (distances)
    distances.sort()
    time_multi = (time.time()-t2)
    return time_multi

def get_distances_classic(x1, points):
    'calculate distance to every other point without mutliprocessing'
    distances = []
    t5 = time.time()
    for p in points:
        distance = calc_distance_classic(x1,p)
        distances.append(distance)
    #print(distances)
    distances.sort()
    time_classic = (time.time()-t5)
    return time_classic


#---------------main-------------------#
number_of_points = [10,100,1000,10000,100000,500000,1000000]
x1= np.array([x for x in range(3)])
time_classic=[]
time_multi=[]
#for x in number_of_points:
   # points = create_points(n=x)
    #time_1 = get_distances_classic(x1,points)
    #time_classic.append(time_1)
    #time_2 = get_distances_multi(x1,points)
    #time_multi.append(time_2)
#print(time_classic)
#print(time_multi)

time_classic = [0.00014328956604003906, 0.0011646747589111328, 0.011996269226074219, 0.10965776443481445, 1.0850849151611328, 5.082998991012573, 9.964872121810913]
time_multi = [0.12496590614318848, 0.12216591835021973, 0.11765193939208984, 0.11903810501098633, 0.4630908966064453, 2.0164098739624023, 4.603604793548584]

plt.plot(number_of_points,time_classic)
plt.plot(number_of_points,time_multi)
plt.ticklabel_format(style="plain")
#plt.show()
#plt.savefig("data.png")

#print(f'Zeit: {(time.time()-t0):.8f}s')
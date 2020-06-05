import numpy as np 
import time
import math
from multiprocessing import Pool




def create_points(n=1000000,dimension=3):
    'creates 3D Points'
    points = 10* np.random.rand(n,dimension)
    #print(points)
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

def get_distances_multi(x1, points):
    'calculate distance to every other point with mutliprocessing'
    distances = []
    t0 = time.time()
    if __name__ == '__main__':
        with Pool(15) as p:
            distance = p.starmap(calc_distance,[(x1,p) for p in points])
            distances.append(distance)
    #print (distances)
    distances.sort()
    print(f'Zeit: {(time.time()-t0):.8f}s')
    return distances

def get_distances_classic(x1, points):
    'calculate distance to every other point without mutliprocessing'
    distances = []
    t0 = time.time()
    for p in points:
        distance = calc_distance_classic(x1,p)
        distances.append(distance)
    #print(distances)
    distances.sort()
    print(f'Zeit: {(time.time()-t0):.8f}s')
    return distances


#---------------main-------------------#
t0=time.time()

x1= np.array([x for x in range(3)])
x2=np.array([1,3,2])
points = create_points()
#get_distances_classic(x1,points)
get_distances_multi(x1,points)

#print(calc_distance(x1,x2))


#print(f'Zeit: {(time.time()-t0):.8f}s')











# def f(x):
#     return x**2

# if __name__ == '__main__':
#     with  Pool(1) as p:
#         print(p.map(f,[1,2,3,4,6,5]))

# t0=time.time()
# print(f'Zeit: {(time.time()-t0):.2f}s')
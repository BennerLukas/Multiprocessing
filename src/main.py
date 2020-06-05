import numpy as np 
import time
import math
from multiprocessing import Pool



def create_points(n=10):
    'creates 3D Points'
    pass
    return points

def calc_distance(x1, x2):
    'calculate distance between 2 Points'
    distance = np.linalg.norm(x1-x2)
    
    return distance

def get_distances_multi(x1, points):
    'calculate distance to every other point with mutliprocessing'
    pass

def get_distances_classic(x1, points):
    'calculate distance to every other point without mutliprocessing'
    pass


#---------------main-------------------#
t0=time.time()

x1= np.array([1,1,1])
x2=np.array([1,3,2])


print(calc_distance(x1,x2))


print(f'Zeit: {(time.time()-t0):.8f}s')











# def f(x):
#     return x**2

# if __name__ == '__main__':
#     with  Pool(5) as p:
#         print(p.map(f,[1,2,3,4,6,5]))

# t0=time.time()
# print(f'Zeit: {(time.time()-t0):.2f}s')
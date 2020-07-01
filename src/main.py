# used libraries:
import numpy as np 
import time
from multiprocessing import Pool



#function definitions:
def create_points(n=1000000,dimension=3):
    print("--Create Points--")
    'creates 3D Points'
    points = 10* np.random.rand(n,dimension)
    return points

def calc_distance(x1, x2):
    'calculate distance between 2 Points'
    distance = np.linalg.norm(x1-x2)
    return distance

def get_distances_multi(x1, points, pools):
    'calculate distance to every other point with mutliprocessing'
    print("--Berechne Abstand (multi)--")
    distances = []
    t0 = time.time()
    if __name__ == '__main__':
        with Pool(pools) as p:
            distance = p.starmap(calc_distance,[(x1,p) for p in points])
            distances.append(distance)
    distances.sort()
    t= time.time()-t0
    print(f'Zeit (multiprocessing): {t:.8f}s')
    return distances, t

def get_distances_classic(x1, points):
    'calculate distance to every other point without mutliprocessing'
    print("--Berechne Abstand (single)--")
    distances = []
    t0 = time.time()
    for p in points:
        distance = calc_distance(x1,p)
        distances.append(distance)
    distances.sort()
    t= time.time()-t0
    print(f'Zeit (singleprocessing): {t:.8f}s')
    return distances, t




#---------------main-------------------#

if __name__ == '__main__':  
    

    # choose number of pools (depending on core count (ideal should be 10))
    pools = int(input("Anzahl Pools: "))
    n = int(input("Anzahl Punkte: "))

    #create data
    x1= np.array([x for x in range(3)]) 
    points = create_points(n)
    # calculate distance serial / classic
    _, t_classic =get_distances_classic(x1,points)

    # calculate distance with mutliprocessing and pools
    _, t_multi =get_distances_multi(x1,points, pools)

    # calculate difference
    print(f"Prozentualer Unterschied: {((1-(t_multi/ t_classic))*100):.2f}%")













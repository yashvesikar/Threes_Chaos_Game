import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

def plot_points(iterations):
    A_x = 10
    A_y = 10
    B_x = 110
    B_y = 10
    C_x = 60
    C_y = 60

    A = (A_x,A_y)
    B = (B_x,B_y)
    C = (C_x,C_y)

    plt.axis([0, 120, 0, 70]) #Axis values [x min/max,y min/max]

    x = [A_x,B_x,C_x]
    y = [A_y,B_y,C_y]

    # Border points
    plt.plot(A_x,A_y,'or')
    plt.plot(B_x,B_y,'or')
    plt.plot(C_x,C_y,'or')

    #Initalizes starting point and plots it
    point_x = np.random.randint(min(x),max(x))
    point_y = np.random.randint(min(y),max(y))
    print(point_x,point_y)
    plt.plot(point_x, point_y,'or')

    point = (point_x,point_y) #Creates point value to overwrite later

    # plt.point(point,'or')

    for i in range(iterations):
        roll = np.random.randint(1,6)
        if (roll == 1) or (roll == 2):
            # step_dst = distance.euclidean(point, A)
            point_x = (point_x + A_x)/2
            point_y = (point_y + A_y)/2
            plt.plot(point_x, point_y,'or')
        elif (roll == 3) or (roll == 4):
            point_x = (point_x + B_x)/2
            point_y = (point_y + B_y)/2
            plt.plot(point_x, point_y,'or')
        else:
            point_x = (point_x + C_x)/2
            point_y = (point_y + C_y)/2
            plt.plot(point_x, point_y,'or')

    plt.show()


plot_points(10000)

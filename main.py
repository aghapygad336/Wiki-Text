


import math
import aaa
import numpy as np
from scipy.spatial.distance import euclidean


mylist = aaa.read("wiki.test.raw")


array = aaa.idftf_table(mylist)

def similarity_matrix(array):
    similarity = np.dot(array.T , array)
    square_mag = np.diag(similarity)
    inv_square_mag = 1 / square_mag
    inv_square_mag[np.isinf(inv_square_mag)] = 0
    inv_mag = np.sqrt(inv_square_mag)
    cosine = similarity * inv_mag
    cosine = cosine.T * inv_mag
    array = cosine
    print(array)
    input()
    for a in range(len(mylist)):
        mine = []
        for i in range(len(mylist)):
            mine.append((mylist[i][0],array[a,i]))
        def getKey(key):
            return key[1]
        print("+++++++++++++++++++++++++++++++++++")

        mine.sort(key=getKey,reverse=True)
        print("Input : ",mine[0])
        print(mine[1])
        print(mine[2])
        print(mine[3])


def k_means(array,k=3,iter=100):
    def calc(a,b):
        return euclidean(a,b)
    array = array.T


    list = []
    for i in range(len(array)):
        list.append( [array[i] ,9999 ,-1])
    c = []
    import random
    for i in range(k):
        c.append(list[random.randint(0, len(list)-1) ][0])
    print(c[0].shape)
    for iterations in range(iter):
        for i in range(k):
            for j in range(len(array)):
                if calc(list[j][0], c[i]) < list[j][1]:
                    list[j][2] = i
                    list[j][1] = calc(array[j], c[i])

        for i in range(k):
            count = 0
            sum = np.zeros(len(array.T))
            for j in range(len(list)):
                if (list[j][2] == i):
                    count += 1
                    sum += list[j][0]
            print(count)
            if count > 0:
                c[i] = sum/float(count)

        print(c)

    for a in range(len(list)):
        mine = []
        for i in range(len(list)):
            mine.append((mylist[i][0],calc(list[a][0],list[i][0])))
        def getKey(key):
            return key[1]
        print("+++++++++++++++++++++++++++++++++++")

        mine.sort(key=getKey)
        print("Input : ",mine[0])
        print(mine[1])
        print(mine[2])
        print(mine[3])

similarity_matrix(array)
input()
k_means(array,k=3)


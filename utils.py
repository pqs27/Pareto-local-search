import time
import math
import matplotlib.pyplot as plt


def get_proportion(Yexact, Yapprox):# Yapprox is a dictionary with v1: v2: 
    return len(set(Yapprox) & set(Yexact))/len(set(Yexact))

"""
def get_score(x):
    return (sum([i["v1"] for i in x]), sum([i["v2"] for i in x]))

def is_dominated(x, y):
    #Returns True if x is dominated by y
    score_x, score_y = get_score(x), get_score(y)
    return score_x[0] <= score_y[0] and score_x[1] <= score_y[1]

def is_score_dominated(score_
    return score_x[0] <= score_y[0] and score_x[1] <= score_y[1]

def get_proportion(Yexact, Yapprox):
    return sum([get_score(v) in Yexact for v in Yapprox]) / len(Yexact)
"""
def d(x, y, p1, p2):
    return math.sqrt(p1 * (x[0] - y[0])**2 + p2 * (x[1] - y[1])**2)

def dprime(A, y, p1, p2):
    return min(d(x, y, p1, p2) for x in A)
"""
def get_distance(Yexact, Yapprox):
    best1, best2 = max(Yexact, key=lambda x: x[0]), max(Yexact, key=lambda x: x[1])
    p1, p2 = 1/abs(best1[0] - best2[0]), 1/abs(best1[1] - best2[1])
    return sum(dprime(Yexact, get_score(y), p1, p2) for y in Yapprox) / len(Yexact)
"""
def get_avg(A, precision=2):
    return round(sum(A) / len(A), precision)

def draw_pts(all_pts,exact):
    
    _x = []
    _y = []
    x_=[]
    y_=[]
    
    for x, y in all_pts:
        _x.append(x)
        _y.append(y)
    for x, y in exact:
        x_.append(x)
        y_.append(y)
        
    plt.plot(_x, _y, 'ro')
    plt.plot(x_, y_)
    plt.grid()
    plt.show()
    
    return 0

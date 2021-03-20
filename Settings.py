import numpy as np


class Settings:
    def __init__(self):
        '''初始化数据设置'''
        self.s_h = 916.9                   #比热
        self.rho = 7000                    #密度
        self.delta_x = 0.01                #空间步长
        self.lamda = 20.3                  #导热系数
        self.L = 250000                    #潜热
        self.T1 = np.array([[[300,300,300,300],[300,300,300,300],[300,300,300,300],[300,300,300,300]],
                   [[300,300,300,300],[300,1370,1370,300],[300,1370,1370,300],[300,300,300,300]],
                   [[300,300,300,300],[300,1370,1370,300],[300,1370,1370,300],[300,300,300,300]],
                   [[300,300,300,300],[300,300,300,300],[300,300,300,300],[300,300,300,300]]],dtype = float)
        self.T2 = np.array([[[300,300,300,300],[300,300,300,300],[300,300,300,300],[300,300,300,300]],
                   [[300,300,300,300],[300,1370,1370,300],[300,1370,1370,300],[300,300,300,300]],
                   [[300,300,300,300],[300,1370,1370,300],[300,1370,1370,300],[300,300,300,300]],
                   [[300,300,300,300],[300,300,300,300],[300,300,300,300],[300,300,300,300]]],dtype = float)
        self.rold = np.array([[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                   [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                   [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                   [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]],dtype = float)
        self.rnew = np.array([[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],dtype = float)
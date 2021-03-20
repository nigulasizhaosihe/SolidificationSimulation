import math
import numpy as np

class Heatcal:
    '''传热主程序'''
    def __init__(self):
        self.drawdata = []
        self.time = []
    def heat_simulation(self,s_h,rho,delta_x,lamda,Told,Tnew,rold,rnew,L):

        endflag = 0                                                          #停止标记
        delta_t = 0.01 * s_h * rho * delta_x * delta_x / (6 * lamda)         #时间步长
        flag = 0                                                             #时间标记
        t = 0                                                                #时间统计
        fsold = np.array([[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],dtype = float) #旧的固相率场
        fsnew = np.array([[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                   [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],dtype = float) #新的固相率场
        ns = 0             #形核数
        while(endflag == 0):
            for i in range(1,3):
                for j in range(1,3):
                    for k in range(1,3):
                        qx = lamda * delta_x * delta_t * (Told[i - 1][j][k] - Told[i][j][k])
                        qy = lamda * delta_x * delta_t * (Told[i][j - 1][k] - Told[i][j][k])
                        qz = lamda * delta_x * delta_t * (Told[i][j][k - 1] - Told[i][j][k])
                        qix = lamda * delta_x * delta_t * (Told[i][j][k] - Told[i + 1][j][k])
                        qiy = lamda * delta_x * delta_t * (Told[i][j][k] - Told[i][j + 1][k])
                        qiz = lamda * delta_x * delta_t * (Told[i][j][k] - Told[i][j][k + 1])
                        q = qx + qy + qz - qix - qiy - qiz
                        Tnew[i][j][k] = Told[i][j][k] + q/(s_h * rho * delta_x * delta_x * delta_x)          #求解当前时刻的温度(不考虑潜热)

                        if(flag >= 52 and fsold[i][j][k] != 1):
                            '''计算生长速度'''
                            rnew[i][j][k] = (0.6462 * (1148 - Told[i][j][k]) * (1148 - Told[i][j][k]) / 1000000) * delta_t + rold[i][j][k]

                            '''计算固相率场'''
                            fsnew[i][j][k] = 1 - math.exp((-4/3) * math.pi * ns * rnew[i][j][k] * rnew[i][j][k] * rnew[i][j][k])

                            '''计算潜热修正后的温度'''
                            delta_fs = fsnew[i][j][k] - fsold[i][j][k]
                            Tplus = delta_fs * L / s_h
                            Tnew[i][j][k] = Tnew[i][j][k] + Tplus

                            '''新场旧场交换'''
                            fsold[i][j][k] = fsnew[i][j][k]
                            rold[i][j][k] = rnew[i][j][k]



            '''时间计数'''
            flag += 1

            '''时间统计'''
            t += delta_t

            #'''将数据写入文件'''
            #a = Tnew[1][1][1]
            #with open('data.txt', 'a') as file_object:
            #    file_object.write(str(a) + '\n')

            '''判断是否停止计算'''
            for i in range(1, 3):
                for j in range(1, 3):
                    for k in range(1, 3):
                        if Tnew[i][j][k] >= 750:
                            pass
                        else:
                            endflag = 1

            '''判断是否形核'''
            if (flag == 52):
                '''计算形核数'''
                ns = ((658200 + 3.814 * ((Tnew[1][1][1] - Told[1][1][1]) / delta_t) * ((Tnew[1][1][1] - Told[1][1][1]) / delta_t)) ** 1.5) * 0.87

            '''将计算出来的新温度赋给旧温度'''
            for i in range(1,3):
                for j in range(1,3):
                    for k in range(1,3):
                        Told[i][j][k] = Tnew[i][j][k]

            self.drawdata.append(Told[1][1][1])
            self.time.append(t)
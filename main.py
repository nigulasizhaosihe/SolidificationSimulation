from Settings import *
from HeatTransferCalculation import *
from drawcoolingcurve import *


class Solidificationsimulation:
    '''计算主程序'''
    def __init__(self):
        self.hs = Heatcal()
        self.settings = Settings()
        self.draw = Drawcoolingcurve()

    def start(self):
        self.hs.heat_simulation(self.settings.s_h,self.settings.rho,self.settings.delta_x,self.settings.lamda,self.settings.T1,self.settings.T2,self.settings.rold,self.settings.rnew,self.settings.L)
        self.draw.draw(self.hs.time,self.hs.drawdata)



if __name__ == '__main__':
    ss = Solidificationsimulation()
    ss.start()




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
        self.hs.heat_simulation(self.settings.s_hL,self.settings.s_hS,self.settings.rhoL,self.settings.rhoS,
                                self.settings.delta_x,self.settings.lamdaL,self.settings.lamdaS,self.settings.T1,
                                self.settings.T2,self.settings.rold,self.settings.rnew,self.settings.L,
                                self.settings.fsold,self.settings.fsnew)

        self.draw.draw(self.hs.time,self.hs.drawdata)



if __name__ == '__main__':
    ss = Solidificationsimulation()
    ss.start()




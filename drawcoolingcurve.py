import matplotlib.pyplot as plt
import HeatTransferCalculation as HC

class Drawcoolingcurve:
    def draw(self,xarr,yarr):
        fig, ax = plt.subplots()
        ax.plot(xarr,yarr)

        plt.show()
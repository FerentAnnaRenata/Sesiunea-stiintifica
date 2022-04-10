import math
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

freq = 500
axa = 10
m = 0.05 * axa
ace = 7500
la = 1
d = 2


class Needle:
    def __init__(self, x=None, y=None, theta=None, length=la):
        if x is None:
            x = random.uniform(0, axa)
        if y is None:
            y = random.uniform(0, axa)
        if theta is None:
            theta = random.uniform(0, math.pi)

        self.center = np.array([x, y])
        self.comp = np.array([length / 2 * math.cos(theta), length / 2 * math.sin(theta)])
        self.endPoints = np.array([np.add(self.center, -1 * np.array(self.comp)), np.add(self.center, self.comp)])

    def intersectsY(self, y):
        return self.endPoints[0][1] < y and self.endPoints[1][1] > y


class Buffon_Sim:
    def __init__(self):
        self.floorboards = []
        self.boards = int((axa / d) + 1)
        self.needles = []
        self.intersections = 0
        # Text
        window = "Buffon"
        title = "Simularea problemei acului a lui Buffon pentru aproximarea lui π"
        desc = (str(ace) + " de ace de lungime " + str(la) +
                " distribuite uniform pe o suprafață de " + str(axa) + " pe " + str(axa) +
                " cu lățimea dreptunghiurilor de " + str(d) + " unități")

        fig = plt.figure(figsize=(8, 8))
        fig.canvas.set_window_title(window)
        fig.suptitle(title, size=16, ha='center')
        self.buffon = plt.subplot()
        self.buffon.set_title(desc, style='italic', size=9, pad=5)
        self.results_text = fig.text(0, 0, self.updateResults(), size=10)
        self.buffon.set_xlim(0 - m, axa + m)
        self.buffon.set_ylim(0 - m, axa + m)
        plt.gca().set_aspect('equal')

    def plotFloorboards(self):
        for j in range(self.boards):
            self.floorboards.append(0 + j * d)
            self.buffon.hlines(y=self.floorboards[j], xmin=0, xmax=axa, color='black', linestyle='--',
                               linewidth=2.0)

    def tossNeedle(self):
        needle = Needle()
        self.needles.append(needle)
        p1 = [needle.endPoints[0][0], needle.endPoints[1][0]]
        p2 = [needle.endPoints[0][1], needle.endPoints[1][1]]
        for k in range(self.boards):
            if needle.intersectsY(self.floorboards[k]):
                self.intersections += 1
                self.buffon.plot(p1, p2, color='blue', linewidth=0.5)
                return

        self.buffon.plot(p1, p2, color='green', linewidth=0.5)

    def plotNeedles(self):
        for i in range(ace):
            self.tossNeedle()
            self.results_text.set_text(self.updateResults(i + 1))
            if (i + 1) % freq == 0:
                plt.pause(1 / freq)

    def updateResults(self, needlesTossed=0):
        if self.intersections == 0:
            sim_pi = 0
        else:
            sim_pi = (2 * la * needlesTossed) / (d * self.intersections)

        return ("Intersectii: " + str(self.intersections) +
                "\nNr total ace: " + str(needlesTossed) +
                "\nAproximarea lui Pi: " + str(sim_pi) )

    def plot(self):
        legend_lines = [mlines.Line2D([], [], color='black', linestyle='--', lw=2),
                        mlines.Line2D([], [], color='blue', lw=1),
                        mlines.Line2D([], [], color='green', lw=1)]
        self.buffon.legend(legend_lines, ['Marginea', 'intersectiile acelor', 'acele care nu se intersecteaza'], loc=1,
                           framealpha=0.9)  # top left and mostly opaque
        self.plotFloorboards()
        self.plotNeedles()
        plt.show()


def main():
    a = Buffon_Sim()
    a.plot()


main()

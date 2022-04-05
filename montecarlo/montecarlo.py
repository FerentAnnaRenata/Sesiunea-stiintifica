
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
matplotlib.use("TkAgg")

fig = figure(figsize=(8, 8), dpi=120)

n = int(10000)
raza = 0.5
nInside = 0
nDrops = 0

coord_x = np.random.default_rng().uniform(0, 1, (n,))
coord_y = np.random.default_rng().uniform(0, 1, (n,))

fig1 = plt.figure(1)
plt.get_current_fig_manager().window.wm_geometry("+00+00")  # move the window
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.legend()

isFirst1 = True
isFirst2 = True

piValueI = []
nDrops_arr = []

insideX = []
outsideX = []
insideY = []
outsideY = []

for i in range(n):
    x = coord_x[i]
    y = coord_y[i]

    nDrops = nDrops + 1

    if ((x-0.5)**2 + (y-0.5)**2) <= raza ** 2:
        nInside = nInside + 1
        insideX.append(x)
        insideY.append(y)

    else:
        outsideX.append(x)
        outsideY.append(y)

    if i % 100 == 0:

        plt.figure(1)

        if isFirst1:

            plt.scatter(insideX, insideY, c='blue', s=50, label='În interior')
            isFirst1 = False
            plt.legend(loc=(0.75, 0.9))
        else:

            plt.scatter(insideX, insideY, c='blue', s=50)

        plt.figure(1)

        if isFirst2:

            plt.scatter(outsideX, outsideY, c='black', s=50, label='În exterior')
            isFirst2 = False
            plt.legend(loc=(0.75, 0.9))
        else:
            plt.scatter(outsideX, outsideY, c='black', s=50)

        arie = 4 * nInside / nDrops
        plt.figure(1)
        plt.title('Nr de puncte luate = ' + str(n) + r';  π  ≈' + str(arie))
        piValueI.append(arie)
        nDrops_arr.append(nDrops)

        plt.pause(0.1)

arie = 4 * nInside / n
print("Valoare estimată a lui Pi: ", arie)
plt.show()

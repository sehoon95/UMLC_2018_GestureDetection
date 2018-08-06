import math
import matplotlib.pyplot as plt
import csv
import numpy as np

ROW_COUNT = 250
START_ROW_COUNT = 0

for j in range(0,100000):

    b = []
    c = []
    d = []
    filename = "Testup.csv"
    with open(filename, 'r', encoding='utf-8') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for idx, row in enumerate(plots):
            if(START_ROW_COUNT <= idx <= ROW_COUNT):
                b.append(float(row[1]))
                c.append(float(row[2]))
                d.append(float(row[3]))

    time = np.arange(len(b))

    if math.trunc(b[0])<=6 and math.trunc(b[1])>6:
        plt.figure(figsize=(5, 5), dpi=100)
        plt.plot(time,b,linestyle='-', marker='.', markersize=1, color='k')
        plt.plot(time,d,linestyle='-', marker='.', markersize=1, color='c')
        plt.plot(time,c,linestyle='-', marker='.', markersize=1, color='m')
        plt.ylim([-20, 20])
        plt.axis('off'), plt.xticks([]), plt.yticks([])
        plt.tight_layout()
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0, wspace=0)
        plt.savefig("up_test1_"+str(j) + ".jpg")
        plt.clf()

    START_ROW_COUNT = START_ROW_COUNT + 1
    ROW_COUNT = ROW_COUNT + 1
    print(START_ROW_COUNT)

import seaborn as sns
import matplotlib.pyplot as plt
import time
import numpy as np
import pandas as pd

# Create a dataset
a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [
    2, 3, 1, 4, 8], [4, 7, 9, 3, 2], [5, 7, 2, 9, 1]]
b = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [
    2, 3, 1, 4, 3], [4, 3, 9, 3, 2], [5, 6, 2, 2, 1]]

# Create Timestamp Matrice
t = np.zeros((5, 5))


def detect(arr):
    for (x, y), element in np.ndenumerate(np.array(arr)):
        if(element > 400 and t[x][y] == 0.0):
            t[x][y] = time.time()
        elif(element > 400 and t[x][y] != 0):
            if(time.time() - t[x][y] > 9):
                print("Alert of Sensor placed at " + str(x) + "," + str(y))
        elif(element <= 400):
            t[x][y] = 0.0

    plt.figure()
    df = pd.DataFrame(arr)
    sns_plot = sns.heatmap(df, annot=True, annot_kws={
                           'size': 9, 'weight': 'bold', }, cmap="YlOrRd", fmt='g')
#     file = open("output.png", "r+")
#     file. truncate(0)
#     file. close()
    sns_plot.figure.savefig("output.png")
    print("done")


i = 0
while (i < 2):
    a = np.random.randint(1000, size=(5, 5))
    detect(a)
    i += 1
    time.sleep(10)
print("Done")

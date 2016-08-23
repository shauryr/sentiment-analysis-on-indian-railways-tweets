import numpy as np
from matplotlib import pyplot as plt

path = '/home/shaurya/data/hackathon/input/negative_scorelist.txt'

import plotly.plotly as py
import plotly.graph_objs as go


def my_dist(x):
    return np.exp(-x ** 2)


# x = np.arange(-100, 100)
x = []
file_path = open(path, 'r')

for i in file_path:
    i = i.rstrip()
    x.append(float(i))

plt.hist(x, bins=100)
plt.title("Tweet Sentiment Histogram")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

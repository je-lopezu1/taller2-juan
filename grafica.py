import random as rand
import matplotlib.pyplot as plt
import numpy as np

def grafica():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, label='sin(x)')
    plt.plot(x, z, label='cos(x)')
    plt.show()

grafica()
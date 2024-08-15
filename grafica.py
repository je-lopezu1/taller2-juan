import random as rand
import matplotlib.pyplot as plt
import numpy as np

def grafica():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)
    k = np.tan(x)
    q = np.arctan(x)
    plt.plot(x, y, label='sin(x)')
    plt.plot(x, z, label='cos(x)')
    plt.plot(x, k, label='tan(x)')
    plt.plot(x, q, label='arctan(x)')
    plt.title('Funciones trigonometricas')
    plt.legend()
    plt.show()

grafica()


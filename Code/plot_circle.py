import numpy as np


def create_circle(center, radius):
    X = np.linspace(0, 7, 1000)
    Y = radius * np.sin(X) + center[1]
    X = radius * np.cos(X) + center[0]
    return X, Y

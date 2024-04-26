import numpy as np


def create_circle(center, radius):
    absisse = np.linspace(0, 7, 1000)
    sin = radius * np.sin(absisse) + center[1]
    cos = radius * np.cos(absisse) + center[0]
    return cos, sin


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    x, y = create_circle((0, 0), 1)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()

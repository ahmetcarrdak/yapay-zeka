import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def intelFace():
    data = np.random.rand(100)

    fig, ax = plt.subplots()
    line, = ax.plot(data)

    def update(data):
        line.set_ydata(data)
        return line,

    def data_gen():
        while True:
            yield np.random.rand(100)

    ani = animation.FuncAnimation(fig, update, data_gen, interval=100, save_count=100)
    plt.show()


intelFace()

"""Graphics Module"""

import matplotlib.pyplot as plt

def graphics(datas, labels):
    """Plot several graph with its labels."""
    plt.figure(figsize=(17, 9))
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.grid(True)

    plt.xlabel('Generaciones')
    plt.title('Algoritmo Genético')

    for data, label in zip(datas, labels):
        x_data = [i for i, _ in enumerate(data)]
        ax1.set_xticks(x_data)
        y_data = data
        #print(data)
        maximum = int(max(data))
        sticks = (i for i in range(0, maximum+1, 2))
        unique_sticks = set(sticks)
        yticsk = sorted(unique_sticks)
        #ax1.set_yticks(yticsk)
        ax1.plot(x_data, y_data, label=label)
    plt.legend()
    plt.show()

def __get_y_ticks(datas):
    maximum = 0
    for data in datas:
        maximum_ = max(data)
        maximum = max(maximum, maximum_)
    tolerance = 2
    rounded_maximum = int(maximum*tolerance)
    sticks = (i for i in range(0, rounded_maximum, 2))
    unique_sticks = set(sticks)
    yticsk = sorted(unique_sticks)
    return yticsk
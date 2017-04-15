import matplotlib.pyplot as plt
from exercise1.logic.settings import Settings

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

def graphic_mma():
    datas, labels = extract_data()
    graphics(datas[:3],labels[:3])

def graphic_ls():
    datas, labels = extract_data()
    graphics(datas[3:4],labels[3:4])

def graphic_r():
    datas, labels = extract_data()
    graphics(datas[4:5],labels[4:5])

def extract_data():
    data = Settings.load_results()
    maximums = [i.maximum for i in data]
    minimums = [i.minimum for i in data]
    averages = [i.average for i in data]
    leasts = [i.least for i in data]
    ranges = [i.range for i in data]

    datas = [maximums, minimums, averages, leasts, ranges]
    labels = ["Maximo", "Minimo", "Promedio", "Cuadrados", "Rango"]
    return datas, labels


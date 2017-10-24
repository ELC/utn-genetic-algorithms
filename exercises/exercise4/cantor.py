import matplotlib.pyplot as plt

def cantor(level=0, inicio=0, fin=1, end=7):
    if level <= -end:
        return
    plt.plot((inicio, fin),(level/2, level/2),'k')
    step = 3**(level-1)
    cantor(level-1, inicio, inicio+step)
    cantor(level-1, fin-step, fin)

cantor()
plt.show()

"""Util Class"""

class Util():
    """Utilities Class, support methods."""
    @staticmethod
    def get_random_prob(precision=2):
        """Return a random probability (between 0 and 1) with given precision."""
        toplimit = 10 ** precision
        percentage = randint(0, toplimit)
        prob = percentage / toplimit
        return prob

    @staticmethod
    def dec_bin(number):
        """ Convert X from Decimal to Binary."""
        return bin(number)[2:]

    @staticmethod
    def find_bigger(array, value):
        """Given a value and a sorted array, find the closest bigger element."""
        for i, j in enumerate(array):
            if value <= j:
                return i

    @classmethod
    def graphics(cls, datas, labels):
        """Plot several graph with its labels."""
        plt.figure(figsize=(17, 9))
        ax1 = plt.subplot2grid((1, 1), (0, 0))
        ax1.grid(True)

        plt.xlabel('Generaciones')
        plt.title('Algoritmo Genético')

        yticks = cls.__get_y_ticks(datas)
        ax1.set_yticks(yticks)

        for data, label in zip(datas, labels):
            x_data = [i for i, _ in enumerate(data)]
            ax1.set_xticks(x_data[::2])
            y_data = data

            ax1.plot(x_data, y_data, label=label)
        plt.legend()
        plt.show()

    @staticmethod
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

if __name__ == "__main__":
    pass
else:
    from numpy.random import randint
    import matplotlib.pyplot as plt

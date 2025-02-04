from matplotlib import pyplot as plt

class Plotter:

    @staticmethod
    def plot_comparator_data(inputs : list, data : dict):

        if isinstance(inputs[0], list):
            inputs = [len(sublist) for sublist in inputs]

        for key, values in data.items():
            plt.plot(inputs, values, label=key)

        plt.legend()
        plt.xlabel("Input Size")
        plt.ylabel("Time (ms)")
        plt.show()

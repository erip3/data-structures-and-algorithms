from comparator import Algorithm_Comparator
from plotter import Plotter
from fibonacci import Fibonacci
from sort import Sort

SORT_INPUTS = [[], [2], [1, 2, 3, 9], [9, 11, 7, 6, 10], [2, 8, 5, 3, 8, 4, 3]]

FIBONACCI_INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def main():
    output = Algorithm_Comparator.compare(Fibonacci, FIBONACCI_INPUTS)
    # output = Algorithm_Comparator.compare(Sort, SORT_INPUTS)
    Plotter.plot_comparator_data(FIBONACCI_INPUTS, output)

if __name__ == '__main__':
    main()
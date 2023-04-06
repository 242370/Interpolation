from Interpolation import Interpolation

if __name__ == '__main__':
    int = Interpolation()
    int.from_function(int.chebyshev_nodes(-1, 1, 10), int.calculate_values(1, int.chebyshev_nodes(-1, 1, 10)), 9)
    int.from_file_plot('Parameters.txt', 3)

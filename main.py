from Interpolation import Interpolation

if __name__ == '__main__':
    int = Interpolation(6)
    # int.from_function(int.chebyshev_nodes(-1, 1, 10), int.calculate_values(1, int.chebyshev_nodes(-1, 1, 10)))
    # int.from_file_plot('Parameters.txt')
    int.from_nodes_plot(int.chebyshev_nodes(-15, 15, 30))

from Interpolation import Interpolation

if __name__ == '__main__':
    inter = Interpolation(1)
    # int.from_function(int.chebyshev_nodes(-1, 1, 10), int.calculate_values(1, int.chebyshev_nodes(-1, 1, 10)))
    # int.from_file_plot('Parameters.txt')
    # int.from_nodes_plot(int.chebyshev_nodes(-10, 10, 6))
    print("If you want to load nodes from files, input 'f'. If not, press 'ENTER'")
    cfile = input()
    if(cfile == 'f'):
        int.from_file_plot('Parameters.txt')
        quit()

    inter.menufunctions()
    function = int(input())
    inter = Interpolation(function)



    print("Choose start of the interpolation section:")
    start = float(input())
    print("Choose end of the interpolation section:")
    end = float(input())
    if (start > end):
        tmp = start
        start = end
        end = tmp
    print("Choose number of Chebyshev nodes:")
    nodes = int(input())

    inter.from_nodes_plot(inter.chebyshev_nodes(start, end, nodes))



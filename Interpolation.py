import numpy as np
import matplotlib.pyplot as plot
from HelperFunctions import getValue


class Interpolation:

    def __init__(self, function):
        # krotka z human-readable nazwami funkcji
        self.functions = ('0.1x\u00b3 - 2x\u00b2 + x + 13', '3sin(x)', '|x|', 'sin(0.1x\u00b3 - 2x\u00b2 + x + 13',
                          '2^(0.1x\u00b3 - 2x\u00b2 + x + 13) - 13', '1.3^(13cos(x) - 1')
        self.data = None
        self.function = function

    def menufunctions(self):
        print("Choose which function's zero you want to find:")
        print("1.Polynomial: " + self.functions[0])
        print("2.Trigonometric Function: " + self.functions[1])
        print("3.Absolute value: " + self.functions[2])
        print("4.Composition of polynomial and trigonometric functions: " + self.functions[3])
        print("5.Composition of polynomial and exponential functions: " + self.functions[4])
        print("6.Composition of trigonometric and exponential functions: " + self.functions[5])

    # Wyznaczanie macierzy współczynników dla wartości z pliku
    def from_file(self, file):
        self.data = np.loadtxt(file, delimiter=' ')
        # Do interpolacji N-tego stopnia potrzeba N + 1 węzłów
        # if power >= len(self.data):
        #     print("Too much power, the reactor won't last")
        #     return
        args = self.data[:, 0]  # wszystkie wiersze, pierwsza kolumna
        values = self.data[:, 1]  # wszystkie wiersze, druga kolumna
        n = len(self.data)  # liczba węzłów
        cols = len(self.data)  # liczba kolumn macierzy, dla stopnia wielomianu n potrzeba n + 1 węzłów
        coefficients = np.zeros([n, cols])  # wyzerowana lista na współczynniki, macierz kształtu 'n' x cols
        coefficients[:, 0] = values  # pierwsza kolumna to wartości węzłów, zgodnie ze wzorem dla 1-szego rzędu
        for col in range(1, cols):  # pierwsza kolumna jest już wypełniona
            for row in range(0, n - col):  # w każdym obiegu głównej pętli będzie o jedną mniej wartość
                coefficients[row][col] = (coefficients[row + 1][col - 1] - coefficients[row][col - 1]) / (args[row + col] - args[row])
        return coefficients

    # Obliczanie wartości wielomianu interpolacyjnego
    def interpolation_polynomial(self, coefficients, x):
        args = self.data[:, 0]  # wszystkie wiersze, pierwsza kolumna
        value = coefficients[0][0]  # wartość wielomianu interpolacyjnego dla danego x
        for col in range(1, len(coefficients[0])):
            multiplier = x - args[0]  # wyrażenie, przez które mnożony będzie współczynnik
            for power in range(1, col):
                multiplier *= (x - args[power])
            value += coefficients[0][col] * multiplier
        return value

    # Obliczanie 'number' węzłów Chebysheva na zadanym przedziale
    def chebyshev_nodes(self, start, end, number):
        args = np.zeros(number)  # przygotowanie wyzerowanej listy 'number'-elementowej
        self.data = np.zeros([number, number])
        for integer_number in range(1, number + 1):
            args[integer_number - 1] = round(0.5 * (start + end) + 0.5 * (end - start) * np.cos((2 * integer_number - 1) * np.pi / (2 * number)), 2)
            self.data[integer_number - 1][0] = args[integer_number - 1]
        return args

    # Obliczanie wartości dla punktów wyznaczonych węzłami Chebysheva
    def calculate_values(self, args):
        values = np.zeros(len(args))
        for arguments in range(len(args)):
            values[arguments] = round(getValue(self.function, args[arguments]), 2)
        return values

    # Wyznaczanie macierzy współczynników dla węzłów Chebysheva
    def from_function(self, args, values):
        # if power >= len(args):
        #     print("Too much power, the reactor won't last")
        #     return
        n = len(args)
        cols = len(values)  # liczba kolumn macierzy, power - najwyższy stopień wielomianu
        coefficients = np.zeros([n, cols])  # wyzerowana lista na współczynniki, macierz kształtu 'n' x cols
        coefficients[:, 0] = values  # pierwsza kolumna to wartości węzłów, zgodnie ze wzorem dla 1-szego rzędu
        for col in range(1, cols):  # pierwsza kolumna jest już wypełniona
            for row in range(0, n - col):  # w każdym obiegu głównej pętli będzie o jedną mniej wartość
                coefficients[row][col] = (coefficients[row + 1][col - 1] - coefficients[row][col - 1]) / (args[row + col] - args[row])
        return coefficients

    # Rysowanie wykresu dla wartości z pliku
    def from_file_plot(self, file):
        self.data = np.loadtxt(file, delimiter=' ')
        args = self.data[:, 0]  # wszystkie wiersze, pierwsza kolumna
        values = self.data[:, 1]  # wszystkie wiersze, druga kolumna
        min_arg = min(args)
        max_arg = max(args)
        plot.scatter(args, values, color='black')
        x_values = np.linspace(min_arg, max_arg, 100)
        y_values = np.zeros(100)
        for i in range(0, 100):
            y_values[i] = self.interpolation_polynomial(self.from_file(file), x_values[i])
        plot.plot(x_values, y_values, color='blue')
        plot.show()

    # Rysowanie wykresu dla wartości z węzłów
    def from_nodes_plot(self, args):
        values = self.calculate_values(args)
        min_arg = min(args)
        max_arg = max(args)
        x_values = np.linspace(min_arg, max_arg, 100)
        plot.scatter(args, values, color='black')
        plot.plot(x_values, self.calculate_values(x_values), color='red', scalex='True')
        y_values = np.zeros(100)  # wartości dla wyliczonego wielomianu
        for i in range(0, 100):
            y_values[i] = self.interpolation_polynomial(self.from_function(args, values), x_values[i])
        plot.plot(x_values, y_values, color='blue', scalex='True')
        plot.show()

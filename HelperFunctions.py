import math as m


# Metoda Hornera: 'x' argument funkcji
# 'wielomian' to lista ze współczynnikami w kolejności od najwyższej potęgi do zerowej (uważać na współczynnik 0)
def horner(wielomian, x):
    wartosc = wielomian[0]

    for i in range(1,
                   len(wielomian)):  # x^3 -2x^2 + 3x + 4 = x(x^2 - 2x + 3) + 4 = x(x(x - 2) + 3) - 4 -> działania po kolei:[[ w[0] * x + w[1] ] * x + w[2] ] * x + w[3]
        wartosc = wartosc * x + wielomian[
            i]  # 1*3 -2 = 1, then 1*3 + 3 = 6, then 6*3 + 4 = 22                                      [[ 1    * 3 + (-2) ] * 3 + 3    ] * 3 + 4

    return wartosc


# Wybór funkcji: 'i' oznacza wybraną funkcję, 'x' wartość argumentu
def getValue(i, x):
    if i == 1:  # x-1
        return x-1
    elif i == 2:  # |x|
        return abs(x)
    elif i == 3:  # 0.5x^3-2x^2+1
        wn = [0.5, -2.0, 0.0, 1.0]
        return horner(wn, x)
    elif i == 4:  # cos(x)
        return m.cos(x)
    elif i == 5:  # |x|*cos(x)
        return m.cos(x) * abs(x)
    elif i == 6:  # 1.3^(13 * cos(x)) - 1
        return 1.3 ** (13 * m.cos(x)) - 1

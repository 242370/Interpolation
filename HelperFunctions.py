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
    wn = [0.1, -2.0, 1.0, 13.0]  # na sztywno wpisane, by użyć w hornerze
    if i == 1:  # 0.1x^3 -2x^2 + x + 13
        return horner(wn, x)
    elif i == 2:  # 3sin(x)
        return 3 * m.cos(x)
    elif i == 3:  # |x|
        return abs(x)
    elif i == 4:  # złożenie nr 1: sin(0.1x^3 -2x^2 + x + 13)
        return m.sin(horner(wn, x))
    elif i == 5:  # złożenie nr 2: 2^(0.1x^3 -2x^2 + x + 13) - 13
        return 2 ** (horner(wn, x)) - 13
    elif i == 6:  # 1.3^(13 * cos(x)) - 1
        return 1.3 ** (13 * m.cos(x)) - 1

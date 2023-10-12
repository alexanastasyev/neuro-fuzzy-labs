import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzzy


def show_func(x, func):
    plt.figure(figsize=(8, 5))
    plt.plot(x, func, 'k', label='ФП')
    plt.ylabel('f')
    plt.xlabel('x')
    plt.ylim(-0.1, 1.1)
    plt.legend(loc=2)
    plt.show()


def show_trimf(x, abc):
    func = fuzzy.trimf(x, abc)
    show_func(x, func)


def show_sigmf(x, b, c):
    func = fuzzy.sigmf(x, b, c)
    show_func(x, func)


def show_pimf(x, a, b, c, d):
    func = fuzzy.pimf(x, a, b, c, d)
    show_func(x, func)


x = np.arange(0, 5.05, 0.1)
show_trimf(x, [1, 2, 3])
show_sigmf(x, 2, 5)
show_pimf(x, 1, 2, 3, 4)

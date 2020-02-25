import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

""" Задача 1 """
x = np.linspace(-3 * np.pi, 3 * np.pi, 201)
plt.plot(x, 0.5 * np.cos(x - 1) + 4)
plt.plot(x, 1.5 * np.cos(x) - 5)
plt.plot(x, 4 * np.cos(x + 1) + 8)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
""" Конец Задачи 1 """

""" Задача 3 """
'''пункт 1'''
ro = float(input('Input RO:'))
fi = float(input('Input coef for calc (fi=coef*Pi):'))
print(f'Ro={ro}, fi={fi}Pi')
x = ro * math.cos(fi * math.pi)
y = ro * math.sin(fi * math.pi)
print(f'x={x}, y={y}')

''' Конец пункта 1'''
""" Конец Задачи 3 """

''' Задача 4'''
''' пункт 1'''


def equations(p):
    x, y = p
    return (y - x ** 2 + 1, np.exp(x) + x - x * y - 1)


x = np.linspace(-2, 4, 201)
plt.plot(x, (np.exp(x) + x - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)
plt.show()

x1, y1 = fsolve(equations, (-2, 1))

print(x1, y1)
'''Конец пункта 1'''
'''Конец Задачи 4'''

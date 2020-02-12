"""
Постройте на одном графике две кривые y(x) для функции двух переменной y(k,x)=cos(k∙x),
 взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1.
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 201)
print(np.poly([1, 1, 2]))
plt.plot(x, np.cos(1*x))
plt.plot(x, np.cos(0.5*x))
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2,2)
plt.grid(True)
plt.show()

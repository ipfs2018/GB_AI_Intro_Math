'''
Задание 2
'''

import numpy


#расчет длины вектора

user_vector=input('Введите через пробел координаты вектора в 3-хмерном пространстве и проходящего через точку(0,0,0)').split()
x=list(map(int,user_vector))
print(x)
user_vector_length=(x[0]**2+x[1]**2+x[2]**2)**0.5
print(f'Длина вектора равна {user_vector_length}.')


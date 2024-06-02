import numpy as np
import json
import os
import matplotlib.pyplot as plt

# Определение функции
def f(x, A):
    return 0.5 + (np.cos(np.sin(x**2 + A**2))**2 - 0.5) / (1 + 0.001*(x**2 + A**2))

# Определение параметров
A = 1.25313
x_start = -100
x_end = 100

# Шаг дискретизации
dx = 0.1

# Создание массива значений x
x = np.arange(x_start, x_end, dx)

# Вычисление значений функции
y = f(x, A)

# Создание директории для результатов, если она не существует
if not os.path.exists('results'):
    os.makedirs('results')

# Сохранение результатов в JSON файл
data = {'x': x.tolist(), 'y': y.tolist()}
with open('results/result.json', 'w') as f:
    json.dump(data, f)

# Построение графика функции
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = 0.5 + (cos^2(sin(x^2 + A^2)) - 0.5) / (1 + 0.001(x^2 + A^2))')
plt.grid(True)
plt.show()

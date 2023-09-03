import matplotlib.pyplot as plt
import numpy as np

client = [0.005, 0.120, 0.675, 2.080, 3.200, 5.000, 9120, 13200]


mongodb_time = [0.308, 0.267, 0.598, 1.435, 2.055, 3.192, 5.652, 7.885]
sql_time = [0.033, 0.088, 0.448, 1.453, 2.284, 3.590, 6.646, 9.310]

plt.plot(client, mongodb_time, marker='o', linestyle='-', color='blue', label='Mongodb')
plt.plot(client, sql_time, marker='s', linestyle='--', color='red', label='SQL')

x_interpolated = np.linspace(min(mongodb_time), max(mongodb_time), 1)  # Создаем 100 равномерно распределенных точек по оси X
y_interpolated = np.interp(x_interpolated, mongodb_time, client)

plt.title('Первый запрос')
plt.xlabel('Количество клиентов')
plt.ylabel('Время выполнения')

plt.legend()
plt.grid(True)
plt.show()
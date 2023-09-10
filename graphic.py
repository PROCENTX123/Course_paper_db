import matplotlib.pyplot as plt
import numpy as np

mongodb_data = [0.002, 0.066, 0.371, 1.144, 1.774, 2.77, 5.066, 7.375]
sqlite_data = [0.0015, 0.046, 0.257, 0.792, 1.229, 1.92, 3.508, 5.106]

mongodb_time = [0.246,
0.416,
1.072,
2.817,
4.092,
6.261,
11.436,
18.042
]
mongodb_ind_time = [0.298,
0.443,
1.160,
2.979,
2.952,
6.782,
12.235,
17.746
]
sql_time = [0.035,
0.267,
1.579,
5.200,
8.007,
12.883,
23.871,
35.918,
]
sql_ind_time = [0.056,
0.230,
1.261,
4.061,
5.773,
9.905,
18.222,
27.856,
]

plt.plot(mongodb_data, mongodb_time, marker='o', linestyle='-', color='blue', label='Mongodb')
plt.plot(mongodb_data, mongodb_ind_time, marker='s', linestyle='--', color='blue', label='Mongodb_ind')
plt.plot(sqlite_data, sql_time, marker='o', linestyle='-', color='red', label='SQL')
plt.plot(sqlite_data, sql_ind_time, marker='s', linestyle='--', color='red', label='SQL_ind')



x_interpolated = np.linspace(min(mongodb_time), max(mongodb_time), 1)  # Создаем 100 равномерно распределенных точек по оси X
y_interpolated = np.interp(x_interpolated, mongodb_time, mongodb_data)


plt.title('Запрос на всю статистику')
plt.xlabel('Размер данных, гб.')
plt.ylabel('Время выполнения, сек.')

plt.legend()
plt.grid(True)
plt.show()
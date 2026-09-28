import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# я использовал здесь дипсик чтобы переобозначить переменные потому что к середине кода я полностью запутался и дальнейшее написание казалось адом

def least_squares(x, y):
    x = np.array(x)
    y = np.array(y)
    slope = ((np.mean(x * y) - np.mean(x) * np.mean(y)) /
             (np.mean(x ** 2) - np.mean(x) ** 2))
    intercept = np.mean(y) - slope * np.mean(x)
    return slope, intercept


data = pd.read_csv(r'C:\Users\LENOVO\PycharmProjects\PythonProject4\iris_data.csv')

sepal_length = data['SepalLengthCm'].values.tolist()
sepal_width = data['SepalWidthCm'].values.tolist()
petal_length = data['PetalLengthCm'].values.tolist()
petal_width = data['PetalWidthCm'].values.tolist()

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

slope_1, intercept_1 = least_squares(sepal_width, sepal_length)
slope_2, intercept_2 = least_squares(petal_length, sepal_length)
slope_3, intercept_3 = least_squares(petal_width, sepal_length)
slope_4, intercept_4 = least_squares(petal_width, petal_length)
slope_5, intercept_5 = least_squares(sepal_width, petal_length)
slope_6, intercept_6 = least_squares(sepal_length, petal_length)

ax1.scatter(sepal_width, sepal_length)
ax1.set_title('Зависимость длины чашелистика от ширины чашелистика')
ax1.grid()

ax2.scatter(petal_length, sepal_length)
ax2.set_title('Зависимость длины чашелистика от длины лепестка')
ax2.axline((0, intercept_2), slope=slope_2, color='red',
           label=f'y = {slope_2:.2f}x + {intercept_2:.2f}')
ax2.grid()
ax2.legend()

ax3.scatter(petal_width, sepal_length)
ax3.set_title('Зависимость длины чашелистика от ширины лепестка')
ax3.axline((0, intercept_3), slope=slope_3, color='red',
           label=f'y = {slope_3:.2f}x + {intercept_3:.2f}')
ax3.grid()
ax3.legend()

ax4.scatter(petal_width, petal_length)
ax4.set_title('Зависимость длины лепестка от ширины лепестка')
ax4.axline((0, intercept_4), slope=slope_4, color='red',
           label=f'y = {slope_4:.2f}x + {intercept_4:.2f}')
ax4.grid()
ax4.legend()

ax5.scatter(sepal_width, petal_length)
ax5.set_title('Зависимость длины лепестка от ширины чашелистика')
ax5.axline((0, intercept_5), slope=slope_5, color='red',
           label=f'y = {slope_5:.2f}x + {intercept_5:.2f}')
ax5.grid()
ax5.legend()

ax6.scatter(sepal_length, petal_length)
ax6.set_title('Зависимость длины лепестка от длины чашелистика')
ax6.axline((0, intercept_6), slope=slope_6, color='red',
           label=f'y = {slope_6:.2f}x + {intercept_6:.2f}')
ax6.grid()
ax6.legend()

plt.tight_layout()
plt.show()


print('Между длиной чашелистика и шириной чашелистика видимая зависимость отсутствует. Зависимости чаши от длины, длины чашелистика от ширины чашелистика расположены умеренно рядом с прямой аппроксимации. Все остальные графики хорошо попадают в область прямой аппроксимации')

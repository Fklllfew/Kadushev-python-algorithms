import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)

x_measured = [304, 320, 332, 352, 368, 400]
y_measured = [60, 65, 68, 70, 75, 80]

x = [304, 400]
y = np.interp(x, x_measured, y_measured)

ax1.scatter(x_measured, y_measured, marker='x')

ax1.errorbar(x_measured, y_measured, yerr=1, xerr=2, color='k', linestyle='None')

ax1.plot(x, y, 'r')

ax1.set_xlabel('U, В', fontsize=14)
ax1.set_ylabel('I, A', fontsize=14)
ax1.set_title('Зависимость напряжения от силы тока', fontsize=16)

ax1.grid()

plt.show()
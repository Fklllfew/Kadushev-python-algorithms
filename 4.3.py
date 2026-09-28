import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')

setosa = 0
versicolor = 0
virginica = 0
x = 0
y = 0
z = 0

for species in df['Species']:
    if species == 'Iris-setosa':
        setosa += 1
    elif species == 'Iris-versicolor':
        versicolor += 1
    elif species == 'Iris-virginica':
        virginica += 1

for length in df['PetalLengthCm']:
    if length <= 1.2:
        x += 1
    elif length > 1.2 and length < 1.5:
        y += 1
    if length >= 1.5:
        x += 1

fig = plt.figure(figsize=(16, 9))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.pie(
    [setosa, versicolor, virginica],
    labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    autopct='%1.1f%%',
)
ax1.set_title('Количество видов')

ax2.pie(
    [x, y, z],
    labels=['<1.2', '>1.2 and <1.5', '>1.5'],
    autopct='%1.1f%%',
)
ax2.set_title('Длинна лепестков')

plt.tight_layout()
plt.show()
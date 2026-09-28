import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

mu, sigma = 0, 1
sample_sizes = [100, 1000, 10000, 100000]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

for ax, n in zip(axes, sample_sizes):
    data = rng.normal(mu, sigma, n)

    ax.hist(data, bins=50, density=True, alpha=0.7,
            color='lightblue', edgecolor='black')

    ax.plot(x, pdf, 'r-', linewidth=2)

    ax.set_title(f'Выборка из {n:,} точек', fontsize=12)
    ax.set_xlabel('Значение')
    ax.grid(alpha=0.3)


plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

figure, axes = plt.subplots(1, 2, figsize=(8, 4))
figure.suptitle("figure")

x = np.linspace(0, 2, 100)

axes1, axes2 = axes

axes1.plot(x, x, label='artist legend')
axes2.plot(x, x ** 5, label='artist legend')

axes1.set_title("axes 1")
axes2.set_title("axes 2")

axes1.set_xlabel("axis x of axes 1")
axes2.set_xlabel("axis x of axes 2")

axes1.set_ylabel("axis y of axes 1")
axes2.set_ylabel("axis y of axes 2")

axes1.legend()
axes2.legend()

axes1.grid()
axes2.grid()


np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)




plt.show()

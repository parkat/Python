import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from pynput.mouse import Listener

xpoints = np.array([.5, 2.3, 2.9])
ypoints = np.array([1.4, 1.9, 3.2])

m = .64
b = 0
print("y-int = " + str(b))
learnRate = .1
epochCount = 0

fig, ax = plt.subplots()
ax.scatter(xpoints, ypoints, color='red', label='Data Points')

colors = cm.rainbow(np.linspace(0, 1, 100))

def update(i):
    global m, b
    y_pred = m * xpoints + b
    error = ypoints - y_pred
    gradient_m = (-2 / len(xpoints)) * sum(xpoints * error)
    gradient_b = (-2 / len(xpoints)) * sum(error)
    m -= learnRate * gradient_m
    b -= learnRate * gradient_b
    ax.plot(xpoints, m * xpoints + b, color=colors[i])
    print(f"slope= {m}\nY-intercept= {b}")





#ani = FuncAnimation(fig, update, frames=range(100), repeat=False)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


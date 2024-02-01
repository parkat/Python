import matplotlib.pyplot as plt
import numpy as np

data = [
    [13, 36],
    [13, 35],
    [5.5, 18],
    [2.7, 8],
    [4.3, 15],
    [12, 25],
    [3.1, 13],
    [6.2, 19],
    [8.8, 26],
    [6.2, 17],
    [8.8, 45],
    [2.7, 12],
    [4, 15],
    [3.3, 12],
    [4.8, 12],
    [4.6, 18],
    [0.5, 7],
    [9.1, 30],
    [6, 16],
    [5.8, 19]
]

data_test = [
    [9, 26],
    [6.25, 17],
    [0.4, 10],
    [2.3, 7],
    [11, 22],
    [8.645, 21],
    [4.52, 34],
    [7, 23]
]

xpoints = np.array([row[0] for row in data])
ypoints = np.array([row[1] for row in data])

test_xpoints = np.array([row[0] for row in data_test])
test_ypoints = np.array([row[1] for row in data_test])

plt.scatter(test_xpoints, test_ypoints, color="blue", marker="+", s=30)
plt.scatter(xpoints, ypoints, color="black", marker="o", s=30)
m_x = np.mean(xpoints)
m_y = np.mean(ypoints)

num = sum((x_i - m_x) * (y_i - m_y) for x_i, y_i in zip(xpoints, ypoints))
den = sum((x_i - m_x) ** 2 for x_i in xpoints)
m = num / den
b = m_y - m * m_x

print(f"slope = {m} \nY intercept = {b}")
plt.axline((m_x,m_y),slope= m, color = "red", linestyle= "--")

plt.show()
import matplotlib.pyplot as plt

lr = 0.01
w1 = 0
w0 = 0
X = [1, 3, 7]
y = [2, 6, 14]

for i in range(len(X)):
    prediction = w1 * X[i] + w0
    w1 += 2 * lr * X[i] * (y[i] - prediction)
    w0 += 2 * lr * (y[i] - prediction)

print(f"w0 = {w0}, w1 = {w1}")

# Изобразим точки

plt.scatter(X, y)
plt.plot(X, [w1 * x + w0 for x in X], color = 'red')
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.show()

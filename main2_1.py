import matplotlib.pyplot as plt


def show_func(x, func):
    plt.figure(figsize=(8, 5))
    plt.plot(x, func, 'k', label='ФП')
    plt.ylabel('f')
    plt.xlabel('x')
    plt.ylim(-0.1, 1.1)
    plt.legend(loc=2)
    plt.show()


terms = ['Низкий', 'Средний', 'Высокий']
ranges = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '35-40']
experts = [
    [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]],
]

counts = [[0 for i in range(3)] for j in range(7)]
print(counts)

for i in range(5):
    for j in range(7):
        counts[j][0] += experts[i][j][0]
        counts[j][1] += experts[i][j][1]
        counts[j][2] += experts[i][j][2]

print(counts)

for i in range(7):
    for j in range(3):
        counts[i][j] /= 5

print(counts)

f_low = [0 for i in range(7)]
f_medium = [0 for i in range(7)]
f_high = [0 for i in range(7)]

for i in range(7):
    for j in range(3):
        f_low[i] = counts[i][0]
        f_medium[i] = counts[i][1]
        f_high[i] = counts[i][2]

print(f_low)
print(f_medium)
print(f_high)

plt.plot(f_low)
plt.plot(f_medium)
plt.plot(f_high)
plt.show()

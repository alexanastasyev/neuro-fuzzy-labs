import matplotlib.pyplot as plt


terms = ['Низкий', 'Средний', 'Высокий']
ranges = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '35-40']


def calculate_neuro_fuzzy_func(matrix):
    for i in range(7):
        for j in range(7):
            if matrix[i][j] == 0:
                matrix[i][j] = 1.0 / matrix[j][i]

    m = [0 for i in range(7)]

    for i in range(7):
        for j in range(7):
            m[i] += matrix[i][j]

    for i in range(7):
        m[i] = 1.0 / m[i]

    print(m)

    m_max = max(m)
    for i in range(7):
        m[i] = m[i] / m_max

    print(m)

    return m


expert_low = [
    [1, 0, 0, 0, 0, 0, 0],
    [2, 1, 0, 0, 0, 0, 0],
    [4, 3, 1, 0, 0, 0, 0],
    [6, 5, 4, 1, 0, 0, 0],
    [7, 6, 4, 3, 1, 0, 0],
    [8, 7, 5, 3, 2, 1, 0],
    [9, 8, 7, 3, 3, 2, 1]
]

expert_medium = [
    [1, 2, 6, 9, 8, 7, 5],
    [0, 1, 5, 8, 7, 5, 3],
    [0, 0, 1, 5, 5, 3, 1],
    [0, 0, 0, 1, 1.0/2, 1.0/5, 1.0/6],
    [0, 0, 0, 0, 1, 1, 1.0/5],
    [0, 0, 0, 0, 0, 1, 1.0/3],
    [0, 0, 0, 0, 0, 0, 1]
]

expert_high = [
    [1, 2, 3, 3, 7, 8, 8],
    [0, 1, 2, 2, 5, 7, 9],
    [0, 0, 1, 3, 4, 6, 7],
    [0, 0, 0, 1, 4, 5, 6],
    [0, 0, 0, 0, 1, 2, 3],
    [0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 1]
]

plt.plot(calculate_neuro_fuzzy_func(expert_low))
plt.plot(calculate_neuro_fuzzy_func(expert_medium))
plt.plot(calculate_neuro_fuzzy_func(expert_high))
plt.show()
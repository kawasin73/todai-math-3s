import numpy as np

MIN = 0.00001


def gradient_descent(initial, diff_fn, alpha):
    current = initial
    count = 0
    while count < 1000000:
        next = next_x(current, diff_fn, alpha)
        sum = 0
        for (i, v) in enumerate(current):
            sum += (v - next[i]) ** 2
        distance = sum ** 0.5
        current = next
        count += 1
        if distance < MIN:
            break
    return (current, count)


def next_x(X, diff_fn, alpha):
    next = []
    for (i, v) in enumerate(X):
        next.append(v - alpha * diff_fn(X, i))
    return next


def diff1(X, i):
    A = [
        [9, 12, -6, -3],
        [12, 41, 2, 11],
        [-6, 2, 24, -8],
        [-3, 11, -8, 62]
    ]
    b = [-27, -42, 32, -23]
    sum = 0
    # vertical
    for (j, v) in enumerate(A):
        # if j == i でも2回足されるから大丈夫
        sum += v[i] * X[j] / 2
    # horizontal
    for (j, v) in enumerate(A[i]):
        sum += v * X[j] / 2
    sum += b[i]
    return sum


def diff2(X, i):
    A = [
        [16, 8, 12, -12],
        [8, 29, 16, 9],
        [12, 16, 29, -19],
        [-12, 9, -19, 35]
    ]
    b = [7, 5, -2, 9]
    sum = 0
    # vertical
    for (j, v) in enumerate(A):
        # if j == i でも2回足されるから大丈夫
        sum += v[i] * X[j] / 2
    # horizontal
    for (j, v) in enumerate(A[i]):
        sum += v * X[j] / 2
    sum += b[i]
    return sum


def diff3(X, i):
    if i == 0:
        return 40 * pow(X[0], 3) + 2 * X[0] - 40 * X[0] * X[1] - 2
    elif i == 1:
        return -20 * pow(X[0], 2) + 20 * X[1]
    else:
        print("invalid i == " + i)
        return 0


def f1(X):
    X = np.array(X)
    A = np.array([
        [9, 12, -6, -3],
        [12, 41, 2, 11],
        [-6, 2, 24, -8],
        [-3, 11, -8, 62]
    ])
    b = np.array([-27, -42, 32, -23])
    return np.dot(X.T, np.dot(A, X)) / 2 + np.dot(b.T, X) + 163


def f2(X):
    X = np.array(X)
    A = np.array([
        [16, 8, 12, -12],
        [8, 29, 16, 9],
        [12, 16, 29, -19],
        [-12, 9, -19, 35]
    ])
    b = np.array([7, 5, -2, 9])
    return np.dot(X.T, np.dot(A, X)) / 2 + np.dot(b.T, X) + 5


def f3(X):
    return (X[0] - 1) ** 2 + 10 * (X[0] ** 2 - X[1]) ** 2


if __name__ == '__main__':
    tests = [[0, 0, 0, 0], [-2, -1, 1, 2], [100, 200, 300, 400]]
    print("== 最急降下法-1 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = gradient_descent(test, diff1, 0.001)
        print("f(x) = ", f1(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    print("== 最急降下法-2== ")
    for test in tests:
        print("initial = ", test)
        (result, count) = gradient_descent(test, diff2, 0.001)
        print("f(x) = ", f2(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    tests = [[0,0], [-1,1], [10, 20]]
    print("== 最急降下法-3 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = gradient_descent(test, diff3, 0.001)
        print("f(x) = ", f3(result))
        print("[x1, x2] = ", result)
        print("count = ", count)
        print()

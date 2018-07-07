import numpy as np
import math

MIN = 0.00001


def fletcher_reeves(X, f, gradient):
    s = -gradient(X)
    count = 0
    while count < 100:
        count += 1
        alpha = linear_search(f(X, s), -1, 1, 0.001)
        nextX = X + alpha * s
        if distance(X, nextX) < MIN:
            X = nextX
            break
        gx0 = gradient(X)
        gx1 = gradient(nextX)
        s = -gx1 + s * np.dot(gx1.T, gx1) / np.dot(gx0.T, gx0)
        X = nextX
    return (X, count)


def bfgs(X, gradient):
    H = np.identity(X.size)
    count = 0
    while count < 100000:
        count += 1
        s = np.dot(np.linalg.inv(H), gradient(X)) * -1
        nextX = X + s
        if distance(X, nextX) < MIN:
            X = nextX
            break
        y = gradient(nextX) - gradient(X)

        H = H - np.dot(H, np.dot(s, np.dot(s.T, H))) / np.dot(s.T, np.dot(H, s)) + np.dot(y, y.T) / np.dot(s.T, y)
        X = nextX
    return (X, count)


def distance(X1, X2):
    diff = X1 - X2
    return np.dot(np.ones(len(diff)), diff ** 2)


def linear_search(f, a, b, diff):
    min = math.inf
    x = a
    while a < b:
        y = f(a)
        if y < min:
            min = y
            x = a
        a += diff
    return x


def searchf1(X, s):
    return lambda a: f1(X + a * s)


def f1(X):
    A = np.array([
        [9, 12, -6, -3],
        [12, 41, 2, 11],
        [-6, 2, 24, -8],
        [-3, 11, -8, 62]
    ])
    b = np.array([-27, -42, 32, -23]).reshape(4, 1)
    return (np.dot(X.T, np.dot(A, X)) / 2 + np.dot(b.T, X) + 163)[0]


def gradient1(X):
    A = np.array([
        [9, 12, -6, -3],
        [12, 41, 2, 11],
        [-6, 2, 24, -8],
        [-3, 11, -8, 62]
    ])
    b = np.array([-27, -42, 32, -23]).reshape(4, 1)
    return np.dot(A, X) + b


def searchf2(X, s):
    return lambda a: f2(X + a * s)


def f2(X):
    A = np.array([
        [16, 8, 12, -12],
        [8, 29, 16, 9],
        [12, 16, 29, -19],
        [-12, 9, -19, 35]
    ])
    b = np.array([7, 5, -2, 9]).reshape(4, 1)
    return (np.dot(X.T, np.dot(A, X)) / 2 + np.dot(b.T, X) + 5)[0]


def gradient2(X):
    A = np.array([
        [16, 8, 12, -12],
        [8, 29, 16, 9],
        [12, 16, 29, -19],
        [-12, 9, -19, 35]
    ])
    b = np.array([7, 5, -2, 9]).reshape(4, 1)
    return np.dot(A, X) + b


def searchf3(X, s):
    return lambda a: f3(X + a * s)


def f3(X):
    return (X[0] - 1) ** 2 + 10 * (X[0] ** 2 - X[1]) ** 2


def gradient3(X):
    return np.array([40 * pow(X[0], 3) + 2 * X[0] - 40 * X[0] * X[1] - 2, -20 * pow(X[0], 2) + 20 * X[1]]).reshape(2, 1)


if __name__ == '__main__':
    tests = [[0, 0, 0, 0], [-2, -1, 1, 2], [100, 200, 300, 400]]
    print("== 共役勾配法-1 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = fletcher_reeves(np.array(test).reshape(4, 1), searchf1, gradient1)
        result = result.reshape(4)
        print("f(x) = ", f1(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    print("== 共役勾配法-2 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = fletcher_reeves(np.array(test).reshape(4, 1), searchf2, gradient2)
        result = result.reshape(4)
        print("f(x) = ", f2(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    tests = [[0, 0], [-1, 1], [10, 20]]
    print("== 共役勾配法-3 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = fletcher_reeves(np.array(test).reshape(2, 1), searchf3, gradient3)
        result = result.reshape(2)
        print("f(x) = ", f3(result))
        print("[x1, x2] = ", result)
        print("count = ", count)
        print()

    tests = [[0, 0, 0, 0], [-2, -1, 1, 2], [100, 200, 300, 400]]
    print("== 準ニュートン法-1 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = bfgs(np.array(test).reshape(4, 1), gradient1)
        result = result.reshape(4)
        print("f(x) = ", f1(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    print("== 準ニュートン法-2 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = bfgs(np.array(test).reshape(4, 1), gradient2)
        result = result.reshape(4)
        print("f(x) = ", f2(result))
        print("[x1, x2, x3, x4] = ", result)
        print("count = ", count)
        print()

    tests = [[0, 0], [-1, 1], [10, 20]]
    print("== 準ニュートン-3 ==")
    for test in tests:
        print("initial = ", test)
        (result, count) = bfgs(np.array(test).reshape(2, 1), gradient3)
        result = result.reshape(2)
        print("f(x) = ", f3(result))
        print("[x1, x2] = ", result)
        print("count = ", count)
        print()

from copy import deepcopy
from functools import reduce
import math

A = [
    [math.inf, 21, 7, 13, 15],
    [11, math.inf, 19, 12, 25],
    [15, 24, math.inf, 13, 5],
    [6, 17, 9, math.inf, 22],
    [28, 6, 11, 5, math.inf]
]


def branch(mat, stack):
    tmp = math.inf
    tmp_list = []
    while len(stack) > 0:
        # r_value, ok_list, ng_list
        step = min(stack, key=lambda v: v[0])
        stack.remove(step)

        if step[0] > tmp:
            continue

        if len(step[1]) == len(mat):
            if step[0] < tmp:
                tmp = step[0]
                tmp_list = step[1]
            continue

        v, minv = get_min(mat, step[1], step[2])
        if minv == math.inf:
            continue

        current = reduce(lambda c, x: c + mat[x[0]][x[1]], step[1], 0)

        # ok version
        ok_list = deepcopy(step[1])
        ok_list.append(v)
        r = relaxation(mat, ok_list, step[2])
        ok_v = current + minv + r
        if ok_v < tmp:
            stack.append((ok_v, ok_list, step[2]))

        # ng version
        ng_list = deepcopy(step[2])
        ng_list.append(v)
        r = relaxation(mat, step[1], ng_list)
        ng_v = current + r
        if ng_v < tmp:
            stack.append((ng_v, step[1], ng_list))
    return tmp, tmp_list


def get_min(mat, ok_list, ng_list):
    mat_range = range(len(mat))
    min = math.inf
    min_v = (0, 0)
    for i in mat_range:
        if i in [v[0] for v in ok_list]:
            continue
        for j in mat_range:
            if j in [v[1] for v in ok_list]:
                continue
            if len([v for v in ng_list if v[0] == i and v[1] == j]) > 0:
                continue
            if mat[i][j] < min:
                min = mat[i][j]
                min_v = (i, j)
    return min_v, min


def relaxation(mat, ok_list, ng_list):
    mat_range = range(len(mat))
    sum = 0
    min_from = {}
    for i in mat_range:
        min = math.inf
        if i in [v[0] for v in ok_list]:
            continue
        for j in mat_range:
            if j in [v[1] for v in ok_list]:
                continue
            if len([v for v in ng_list if v[0] == i and v[1] == j]) > 0:
                continue
            if mat[i][j] < min:
                min = mat[i][j]
        min_from[i] = min
        sum += min
    for i in mat_range:
        min = math.inf
        if i in [v[1] for v in ok_list]:
            continue
        for j in mat_range:
            if j in [v[0] for v in ok_list]:
                continue
            if len([v for v in ng_list if v[0] == j and v[1] == i]) > 0:
                continue
            if mat[j][i] - min_from[j] < min:
                min = mat[j][i] - min_from[j]
        sum += min
    return sum


def format_result(ok_list):
    result = "1"
    cur = 0
    for i in range(len(ok_list)):
        for v in ok_list:
            if v[0] == cur:
                result += " -> " + str(v[1] + 1)
                cur = v[1]
                break
    return result


if __name__ == '__main__':
    min_value, min_list = branch(A, [(relaxation(A, [], []), [], [])])
    print("min   : ", min_value)
    print("route : ", format_result(min_list))

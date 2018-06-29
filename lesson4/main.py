import math


def dijkstra(routeMap):
    s = []
    sb = list(range(len(routeMap)))
    distance = [math.inf] * len(routeMap)
    distance[0] = 0
    fromList = [0] * len(routeMap)

    while len(s) != len(routeMap):
        v = 0
        min = math.inf
        for i in sb:
            if distance[i] < min:
                v = i
                min = distance[i]
        s.append(v)
        sb.remove(v)

        for i in sb:
            d = routeMap[v][i]
            if d != 0 and distance[v] + d < distance[i]:
                distance[i] = distance[v] + d
                fromList[i] = v

    # build result route
    cur = len(routeMap) - 1
    result = [cur + 1]
    while cur != 0:
        cur = fromList[cur]
        result.append(cur + 1)
    result.reverse()
    return result


if __name__ == '__main__':
    result = dijkstra(
        [
            [0, 50, 80, 0, 0],
            [0, 0, 20, 15, 0],
            [0, 0, 0, 10, 15],
            [0, 0, 0, 0, 50],
            [0, 0, 0, 0, 0],
        ]
    )
    print(result)

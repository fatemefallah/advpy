def calculator(n, m, ls):
    res = list()
    answer = 0
    i = 0
    while i < n:
        res.append(sum(ls[i: i + m]))
        i += m
    for j in range(len(res)):
        if j % 2 == 0:
            answer += res[j]
        else:
            answer -= res[j]
    return answer


# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))  # [6, 15, 15] 6
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))

def calculator(n, m, ls):
    res = list()
    fin = list()
    # slicing items to m-no list
    i = 0
    while i < n:
        res.append(sum(ls[i: i + m]))
        i += m

    for j in range(len(res) - 1):
        i = j + 1
        if j % 2 == 0:
            res[i] = res[j] - res[i]
        else:
            res[i] = res[i] + res[j]
    return res[-1]


# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))  # [6, 15, 15] 6
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))

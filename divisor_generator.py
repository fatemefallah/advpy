def divs(a):
    res = []
    for i in range(1, int(a) + 1):
        if a % i == 0:
            yield i
            res.append(i)
    return res


"""
def divs(a):
    for i in range(1, a + 1):
        if a % i == 0:
            yield i
"""
def fact(a):
    res = 1
    for i in range(1, a + 1):
        res = i * res
    return res

def comb(n, k):
    numerator = fact(n)
    denominator = fact(k) * fact(n - k)
    res = numerator / denominator
    return int(res)

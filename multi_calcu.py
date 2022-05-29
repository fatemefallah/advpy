def calc(arr):
    arr.sort()
    n = len(arr)

    avg = sum(arr) / n
    maxim = max(arr)
    if n % 2 == 0:
        med = (arr[(n // 2) - 1] + arr[(n // 2)]) / 2
    else:
        med = arr[((n + 1) // 2) - 1]
    res = avg, med, maxim
    return res

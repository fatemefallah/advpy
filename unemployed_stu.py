import re


def solve(arr):
    res = arr.replace(' ', '')
    res = re.split(r'[+=]', res)
    for i in range(len(res)):
        x = 0
        y = 0
        if re.match(r'#+|(\d)+#', res[i]):  # finding char with #
            x = res[i]
            spl = re.split(r'#', x)
            t1 = spl[0]
            t2 = spl[1]
            if i == 2:
                y = int(res[0]) + int(res[1])
                if re.match(rf'^{t1}.*{t2}$', str(y)):
                    return f'{res[0]} + {res[1]} = {y}'
                else:
                    return {'-1'}
            elif i == 1:
                y = int(res[2]) - int(res[0])
                if re.match(rf'^{t1}.*{t2}$', str(y)):
                    return f'{res[0]} + {y} = {res[2]}'
                else:
                    return -1
            else:
                y = int(res[2]) - int(res[1])
                if re.match(rf'^{t1}.*{t2}$', str(y)):
                    return f'{y} + {res[1]} = {res[2]}'
                else:
                    return -1


inp = input()
print(solve(inp))

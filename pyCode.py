import re


def solve(path):
    cnt = 0
    with open(path, 'r') as file:
        for row in file:
            line = str(row).strip()
            if not re.match(r'^#|^$', line):
                cnt += 1
    return cnt


path1 = 'karim_names.py'
print(solve(path1))

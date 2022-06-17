import os
import re


def explore(ttype, address):
    ttype = ttype.lower()
    dic = {}
    cnt = 0
    tmp = list(os.walk(address))
    adds = [x[0] for x in tmp]
    files = [x[2] for x in tmp]
    for i in range(len(files)):
        for j in range(len(files[i])):
            files[i][j] = files[i][j].lower()
            match = re.search(f'\.{ttype}$', files[i][j])
            if match:
                cnt += 1
                dic[adds[i]] = cnt
        cnt = 0
    return dic


print(explore("pY", ".\\CSV"))

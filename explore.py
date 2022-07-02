import os
import re


def explore(ttype, address):
    ttype = ttype.lower()
    dic = {}
    cnt = 0
    tmp = list(os.walk(address))
    print(tmp)
    adds = [x[0] for x in tmp]
    files = [x[2] for x in tmp]
    for i in range(len(files)):
        for j in range(len(files[i])):
            files[i][j] = files[i][j].lower()
            match = re.search(f'\.{ttype}$', files[i][j])   # in this line, the entire title and ext will convert to
            # lowercase. Quera did it better. at the end of my code
            if match:
                cnt += 1
                dic[adds[i]] = cnt
        cnt = 0
    return dic


print(explore("pY", ".\\CSV"))

"""
import os
 
def explore(extension, addr):
    result = dict()
    for obj in os.walk(addr):
        for name in obj[2]:
            if "." in name and name.split('.')[-1].lower() == extension.lower():
                try:
                    result[obj[0]] += 1
                except KeyError:
                    result[obj[0]] = 1
    return result
"""
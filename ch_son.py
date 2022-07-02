import json


dic = {}
inputs = list()
n = int(input())

for i in range(n):
    inp = input()
    inputs.append(inp)
print(dic)
for i in range(len(inputs)):
    if '[' in inputs[i] and not "print" in inputs[i]:
        inp = inputs[i].split(':=')
        arg, dic[arg] = inp[0].strip(), json.loads(inp[1])

    elif '{' in inputs[i]:
        inp = inputs[i].strip().split(':=')
        arg, dic[arg] = inp[0].strip(), json.loads(inp[1])

    elif 'print' in inputs[i]:
        inp = inputs[i].replace('print', '').strip()
        if '[' and '"' in inp:
            arg, key = str(inp[0]), str(inp[3])
            print(dic[arg][key])
        elif not '"' in inp:
            arg, key = str(inp[0]), int(inp[2])
            print(dic[arg][key])
print(dic)


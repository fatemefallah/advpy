inp = input()
inp = inp.strip('=')
res = []
for i in inp:
    if i != '=' and len(inp) != 0:
        res.append(i)
    elif i == '=':
        res.pop()
#salam
   #salam
print(''.join(res))

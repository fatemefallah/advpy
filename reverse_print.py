inp = []
n = int(input())
while n != 0:
    inp.append(n)
    n = int(input())
inp.reverse()
for i in range(len(inp)):
    print(inp[i])

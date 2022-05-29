n, m = map(int, input().split())
k = int(input())
ground = []

for x in range(n):
    ground.append([])
    for y in range(m):
        ground[x].insert(y, int(0))

for i in range(k):
    inp1, inp2 = map(int, input().split())
    ground[inp1 - 1][inp2 - 1] = '*'

    if 0 <= inp1 - 2 < n and 0 <= inp2 - 2 < m and ground[inp1 - 2][inp2 - 2] != '*':
        ground[inp1 - 2][inp2 - 2] += 1

    if 0 <= inp1 - 2 < n and 0 <= inp2 - 1 < m and ground[inp1 - 2][inp2 - 1] != '*':
        ground[inp1 - 2][inp2 - 1] += 1

    if 0 <= inp1 - 2 < n and 0 <= inp2 < m and ground[inp1 - 2][inp2] != '*':
        ground[inp1 - 2][inp2] += 1

    if 0 <= inp1 - 1 < n and 0 <= inp2 - 2 < m and ground[inp1 - 1][inp2 - 2] != '*':
        ground[inp1 - 1][inp2 - 2] += 1

    if 0 <= inp1 - 1 < n and 0 <= inp2 < m and ground[inp1 - 1][inp2] != '*':
        ground[inp1 - 1][inp2] += 1

    if 0 <= inp1 < n and 0 <= inp2 - 2 < m and ground[inp1][inp2 - 2] != '*':
        ground[inp1][inp2 - 2] += 1

    if 0 <= inp1 < n and 0 <= inp2 - 1 < m and ground[inp1][inp2 - 1] != '*':
        ground[inp1][inp2 - 1] += 1

    if 0 <= inp1 < n and 0 <= inp2 < m and ground[inp1][inp2] != '*':
        ground[inp1][inp2] += 1

for i in range(n):
    for j in range(m):
        print(ground[i][j], end=' ')
    print()

"""
n, m = map(int, input().split())
base = [[0] * (m+2) for i in range(n+2)]
k = int(input())
for i in range(k):
	x, y = map(int, input().split())
	base[x][y] = '*'

def check(x ,y):
    pos = [-1, 0, +1]
    if base[x][y] != '*':
        for i in pos:
            for j in pos:
                if i!=0 or j!=0:
                    if base[x+i][y+j] == '*':
                        base[x][y] += 1


for i in range(1,n+1):
	for j in range(1,m+1):
		check(i,j)
for i in range(1,n+1):
	for j in range(1,m+1):
		print(base[i][j], end=' ')
	print('')
	"""
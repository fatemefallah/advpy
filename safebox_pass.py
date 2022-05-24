k = int(input())
passcode = input()
cir = []
ans = 0
for i in range(k):
    cir.append(input())
    moves = cir[i].find(passcode[i])
    ans += min(moves, 9 - moves)
print(ans)
'''
k = int(input())
code = input()
ans = 0
for i in code:
	dial = input()
	moves = dial.find(i)
	ans = ans + min(moves, 9 - moves)
print(ans)
'''
n = int(input())
ans = 0
for i in range(n):
    s = input()
    t = ''
    for ch in s:
        if ch not in t:
            t += ch 
    if ans < len(t):  # ans = max(ans, len(t))
        ans = len(t)
print(ans)

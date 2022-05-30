n = int(input())
names = []
for i in range(n):
    f, l = input().split()
    names.append(f)


def most_freq(List):
    dic = {}
    count, it = 0, ''
    for item in List:
        dic[item] = dic.get(item, 0) + 1
        if dic[item] >= count:
            count, itm = dic[item], item

    if all(value == 1 for value in dic.values()):
        return 1
    return count


print(most_freq(names))


"""n = int(input())
dic = {}
col = 1
for i in range(n):
    f, l = input().split()
    if f in dic:
        col += 1
    else:
        dic[f] = l
print(col)"""

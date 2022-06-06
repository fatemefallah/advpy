def process(path):
    ans = open('ans.csv', 'w')
    with open(path) as csv:
        for row in csv.readlines():
            tmp = row.rstrip().split(',')
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i])
            tmp.append(sum(tmp))
            for i in range(len(tmp)):
                tmp[i] = str(tmp[i])
            ans.write('{}\n'.format(', '.join(tmp)))
    ans.close()

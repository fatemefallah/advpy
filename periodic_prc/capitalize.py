def capitalize(names):
    res = list()
    for name in names:
        res.append(' '.join(i.capitalize() for i in name.split())) # names[i] = names[i].title()
    return res


inp = ['nazaNIN ZAHRA', 'ALI GHOLI KHANE bozorg']
print(capitalize(inp))

def fruits(fruit_list):
    res = {}
    for i in range(len(fruit_list)):
        if fruit_list[i]['shape'] == 'sphere' and \
                300 <= fruit_list[i]['mass'] <= 600 and \
                100 <= fruit_list[i]['volume'] <= 500:
            if fruit_list[i]['name'] in res:
                res[fruit_list[i]['name']] += 1
            else:
                res[fruit_list[i]['name']] = 1
    return res


fruit = (
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})
# {'apple': 2, 'lemon': 1}
print(fruits(fruit))

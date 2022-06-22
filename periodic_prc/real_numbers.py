import re


def real_numbers(numbers):
    res = list()
    for no in numbers:
        if re.match('^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$', no):
            res.append('LEGAL')
        else:
            res.append('ILLEGAL')
    return res


print(real_numbers(['14.5e+2', '3.', '1.1.1', '1+e5']))

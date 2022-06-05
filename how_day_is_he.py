from datetime import datetime


def day_calculator(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    sajjad_bdate = datetime.strptime("1999-01-14", '%Y-%m-%d')
    flag = (date - sajjad_bdate).days
    if flag < 0:
        res = "Not yet born"
    else:
        res = flag
    return res

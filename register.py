def check_registration_rules(**kwargs):
    res = []
    for username, password in kwargs.items():
        if len(username) >= 4 and len(password) >= 6 and username != 'quera' \
                and username != 'codecup' and password.isdigit() == False:
            res.append(username)
    return res


""" invalids = ['quera', 'codecup']
    for item in kwargs:
        if not item in invalids and len(item) > 3 and len(kwargs[item]) > 5 and not kwargs[item].isdigit():
"""
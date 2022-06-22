import re


def is_valid(c):
    return re.match('[\w ]', c) is not None


def invalidation_content(cont):
    length = len(cont)
    cnt = 0
    for char in cont:
        if is_valid(char) is False:
            cnt += 1

    if len(re.findall('spam', cont.lower())) != 0:
        spam = True

    if cnt > (length / 2) and spam:
        invalidation = True
    else:
        invalidation = False

    return invalidation


sender = input()
content = input()

invalid_cont = invalidation_content(content)
invalid_sender = sender.isnumeric()

if invalid_sender is True:
    if invalid_cont is False:
        print('Invalid Sender')
    elif invalid_cont is True:
        print('Fully Invalid')

if invalid_sender is False:
    if invalid_cont is True:
        print('Invalid Content')
    elif invalid_cont is False:
        print('Not Spam')

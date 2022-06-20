import os
import re
import sys
import time


def mk_year_dir(destination, years, postfix):
    years_dir = os.path.join(destination, years)
    if not os.path.exists(years_dir):  # if years folders not exist:
        os.mkdir(years_dir)

    postfix_dir = os.path.join(destination, years, postfix)
    if not os.path.exists(postfix_dir):  # if postfix folders not exist:
        os.mkdir(postfix_dir)


src, des = os.path.join(sys.argv[1]), os.path.join(sys.argv[2])
if not os.path.exists(des):
    os.mkdir(des)

# searching for jpg/mkv files
for obj in os.walk(src):
    for name in obj[2]:

        # finding the year
        year = (time.ctime(os.path.getmtime(os.path.join(obj[0], name))).split(" "))[-1]

        # extract the postfix of files
        if re.match(f'.+\..+$', name):
            post = name.split('.')[-1].lower()
            photo = re.search(f'jpg|jpeg|png$', post)

            if photo:
                mk_year_dir(des, year, 'photos')
                with open(os.path.join(obj[0], name), 'rb') as first:
                    data = first.read()
                    with open(os.path.join(des, year, 'photos', name), 'wb') as second:
                        second.write(data)

            video = re.search(f'mp4|avi|3gp|mpeg|mkv|wmv|mov$', post)
            if video:
                mk_year_dir(des, year, 'videos')
                with open(os.path.join(obj[0], name), 'rb') as first:
                    data = first.read()
                    with open(os.path.join(des, year, 'videos', name), 'wb') as second:
                        second.write(data)

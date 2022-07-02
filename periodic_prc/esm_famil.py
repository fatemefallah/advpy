import csv

esm = {}
famil = {}
keshvar = {}
rang = {}
ashia = {}
ghaza = {}
result = []
participants = []
fields = [esm, famil, keshvar, rang, ashia, ghaza]


def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def ready_up():
    with open('esm_famil_data.csv') as f:
        for piece in read_in_chunks(f):
            # process data
            print(piece)
    '''with open('esm_famil_data.csv') as file:
        for row in file:
            yield row'''


def add_participant(*participant, **answers):
    name = list(answers.items())[0][1]
    ans = list(answers.items())[1][1]
    # res[name] = ans
    participants.append(name)
    esm[name] = ans['esm']
    famil[name] = ans["famil"]
    keshvar[name] = ans["keshvar"]
    rang[name] = ans["rang"]
    ashia[name] = ans["ashia"]
    ghaza[name] = ans["ghaza"]


def has_same(values, field):
    if field in list(values):
        # print("dupli")
        return True
    else:
        # print("no dupli")
        return False


def get_points(point):
    result.append(point)


def calculate_all():
    for item in fields:
        none = all(item.values())
        for player in item.keys():
            if none:
                if has_same(item.values(), item[player]):
                    get_points(5)
                elif not has_same(item.values(), item[player]):
                    get_points(10)
            else:
                if has_same(item.values(), item[player]):
                    get_points(10)
                elif not has_same(item.values(), item[player]):
                    get_points(15)


ready_up()
add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
calculate_all()
print(result)


'''player_list = list(res.keys())
    answers_list = list(res.values())
    for i in range(len(player_list)):
        print(player_list[i])
        test = answers_list[i].values()
        print(test)
        for j in range(len(test)):
            print(list(test)[j])

    print(player_list)
    print(answers_list)'''

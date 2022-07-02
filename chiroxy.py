class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function



def transform_exceptions(func_ls):
    res = list()
    for i in range(len(func_ls)):
        try:
            func_ls[i]()
        except Exception as e:
            exobj = ExceptionProxy(str(e), func_ls[i])
        else:
            exobj = ExceptionProxy("ok!", func_ls[i])
        res.append("msg: " + exobj.msg + "\nfunction name: " + exobj.function.__name__)
    return '\n'.join(res)



def f():
    raise NameError('salam')

def g():
    raise ValueError

def h():
    raise ZeroDivisionError

def f1():
    1 / 1

def g1():
    int("salam")

def h1():
    "salam" + 1

print(transform_exceptions([f, g, h, f1, g1, h1]))

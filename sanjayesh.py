def decorator(validator):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            returned_value = validator(*args, **kwargs)
            if returned_value:
                return func(*args, **kwargs)
            else:
                return 'error'
        return wrapper
    return inner_func

def validator(x):
    return x > 0

@decorator(validator)
def f(x):
    return x ** 2

print(f(4)) #should print 2.0
print(f(-4)) #should print error

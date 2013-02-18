from functools import wraps

def validate(func):
    @wraps(func)
    def wrapper(*args):
        for num in args:
            try:
                int(num)
            except:
                return None
        return func(*args)

    return wrapper

@validate
def add_num(*args):
    total = 0
    for num in args:
        total += num
    return total


print add_num(1,2,3)
print add_num(1,2,"asd")
print add_num(1,2,None)


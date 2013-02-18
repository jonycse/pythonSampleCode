from functools import wraps

def custom_memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print "Returning cache data"
            return cache[args]
            # If result not found then call the function
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@custom_memoize
def add(x,y):
    return x+y

print add(1,2)
print add(2,5)
print add(1,2)
print add(2,5)


# 1
import time
N = 1000000


def decorator_time(fn):
    def wrapper():
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        return dt
    return wrapper


def pow_2():
    return 1000000 ** 2


def in_build_pow():
    return pow(1000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)
mean_pow_2 = 0
mean_in_build_pow = 0
for i in range(N):
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

print(f"Function {pow_2} executed {N} times. Mean time of execution: {mean_pow_2 / N:.10f}")
print(f"Function {in_build_pow} executed {N} times. Mean time of execution: {mean_in_build_pow / N:.10f}")
# Example


# 2
def counter(func):
    count = 0

    def wrapped_counter(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count = count + 1
        print(f'Function was called {count} times in total')
    return wrapped_counter


@counter
def decorated_counter():
    print('')


decorated_counter()
decorated_counter()
decorated_counter()
# Example


# 3
def cache(func):
    cache_dict = {}

    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Adding result in cache: {cache_dict[num]}")
        else:
            print(f"Returning result from cache: {cache_dict[num]}")
        print(f"Cache {cache_dict}")
        return cache_dict[num]
    return wrapper


@cache
def f(n):
    return n * 123456789


f(int(input('Enter your number: ')))
f(int(input('Enter your number: ')))
f(int(input('Enter your number: ')))
f(int(input('Enter your number: ')))
# Example


# 4
USERS = ['admin', 'guest', 'director', 'root', 'superstar']
yesno = input("If you want to authorize enter Y: ")
auth = yesno == 'Y'


def is_auth(func1):
    def wrapper():
        if auth:
            print('User authorized')
            func1()
        else:
            print("User is not authorized. Function won't run")
    return wrapper


def has_access(func2):
    def wrapper():
        access = input('Enter your login: ')
        if access in USERS:
            print('Your login is confirmed')
            func2()
        else:
            print('Login', access, "doesn't exist")
    return wrapper


@is_auth
@has_access
def from_db():
    print('Some data from database')


from_db()
# Example

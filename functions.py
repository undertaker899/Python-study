# 1
def division(num_1, num_2):
    if num_1 % num_2 == 0:
        print('num_2 is divider of num_1')
    else:
        print('num_2 is not divider of num_1')


division(2, 4)
# Example


# 2
def reverse_ladder(n):
    for i in range(n, 0, -1):
        print('*' * i)


reverse_ladder(5)
# Example


# 3
def div_cnt(num, count=0):
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    return count


print(div_cnt(100))
# Example


# 4
def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    if s == s[::-1]:
        print('Input is palindrome')
    else:
        print('Input is not palindrome')


palindrome(input("Enter your string:"))
# Example


# 5
x = 3


def func():
    global x
    print(x)
    x = 5
    x = x + 5
    return x


func()
print(x)
# Example


# 6
def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul


two_mul = get_mul_func(2)
print(two_mul(int(input("Enter your number:"))))
# Example


# 7
def multiple(*nums):
    mul = 1
    for n in nums:
        mul = mul * n
    return mul


print(multiple(2, 2, 2, 2))
# Example


# 8
def correct_func(name_arg=None):
    if name_arg is None:
        name_arg = []
    print(name_arg)
    name_arg.append('first change')
    print(name_arg)
    name_arg.append('second change')
    print(name_arg)


correct_func(name_arg=[123, 1])
# Example


# 9
def nat_num(num=int(input('Enter a number you want to start from: ')), step=int(input('Enter a step: '))):
    while True:
        yield num
        num = num + step


for a in nat_num():
    print(a)
# Example


# 10
def massive(t):
    t_values = t.copy()
    while True:
        value = t_values.pop(0)
        t_values.append(value)
        yield value


for a in massive([1, 2, 3]):
    print(a)
# Example


# 11
def make_adder(num_1):
    def adder(num_2):
        return num_1 + num_2
    return adder


add_input = make_adder(int(input('First number: ')))
print('Sum =', add_input(int(input('Second number: '))))
# Example

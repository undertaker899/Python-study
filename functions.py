# 1
def division(num_1, num_2):
    if num_1 % num_2 == 0:
        print('Second number is divider of first number')
    else:
        print('Second number is not divider of first number')


division(int(input('Enter first number: ')), int(input('Enter second number: ')))
# Example


# 2
def reverse_ladder(n):
    for i in range(n, 0, -1):
        print('*' * i)


reverse_ladder('Enter number of steps reverse ladder will have: ')
# Example


# 3
def div_cnt(num, count=0):
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    return count


print('Number of dividers of your number =', (div_cnt(int(input('Enter your number: ')))))
# Example


# 4
def palindrome(s):
    s = s.lower().replace(' ', '')
    if s == s[::-1]:
        print('Input is palindrome')
    else:
        print('Input is not palindrome')


palindrome(input('Enter your string: '))
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
print(two_mul(int(input('Enter your number: '))))
# Example


# 7
def multiple(*nums):
    mul = 1
    for n in nums:
        mul = mul * n
    return mul


print(multiple(int(input('1st num: ')), int(input('2nd num: ')), int(input('3rd num: ')), int(input('4th num: '))))
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


# 12
def quadratic_equation(a1, a2, a3):
    discriminant = a2**2 - 4*a1*a3
    if discriminant < 0:
        return 'No real roots'
    elif discriminant == 0:
        return -a2/(2*a1)
    else:
        return (-a2 - discriminant**0.5)/(2*a1), (-a2 + discriminant**0.5)/(2*a1)


print(quadratic_equation(int(input()), int(input()), int(input())))
# Example


# 13
def even_numbers(a_num):
    return a_num % 2 == 0


result = filter(even_numbers, [-2, -1, 0, 1, -3, 2, -3])
print(list(result))
# Example


# 14
data = [(82, 191), (68, 174), (90, 189), (73, 179), (76, 184)]
print(sorted(data, key=lambda height_weight: height_weight[0] / (height_weight[1] ** 2)))
# Example

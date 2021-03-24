# 1
a = int(input('Enter current year: '))
leap_year = a % 4 == 0
print("It's", leap_year is True, "that right now is leap year")
# Example


# 2
a, b = int(input('a: ')), int(input("b: "))
if a % 2 == 1 and b % 2 == 1:
    print('a and b are odd numbers')
elif a % 2 == 1 or b % 2 == 1:
    print('a or b is even number')
else:
    print('a and b are even numbers')
# Example

# 3
x_c = int(input('Enter x coordinate: '))
y_c = int(input('Enter y coordinate: '))
if x_c > 0 and y_c > 0:
    print('First quarter')
elif x_c > 0 > y_c:
    print('Fourth quarter')
elif x_c < 0 < y_c:
    print('Second quarter')
elif x_c < 0 and y_c < 0:
    print('Third quarter')
else:
    print('One or both of coordinates is/are zero')
# Example


# 4
speed = int(input('Enter wind speed in meters/seconds: '))
if 0 <= speed <= 4:
    print('Weak wind')
if 5 <= speed <= 10:
    print('Moderate wind')
if 11 <= speed <= 18:
    print('Strong wind')
if speed >= 19:
    print('Hurricane')
# Example


# 5
user = input('Enter your username: ')
user_database = {'user': 'password', 'iseedeadpeople': 'greedisgood', 'hesoyam': 'tgm'}
if user in user_database.keys():
    password = input('Enter your password: ')
    if password in user_database.values():
        print('Welcome', user)
    else:
        print('Invalid password')
else:
    print('No profile with such username')
# Example


# 6
num_1, num_2, num_3 = int(input('First number: ')), int(input('Second number: ')), int(input('Third number: '))
if num_1 < 45 <= num_2 <= num_3:
    print('One number is less than 45')
elif num_2 < 45 <= num_1 <= num_3:
    print('One number is less than 45')
elif num_3 < 45 <= num_1 <= num_2:
    print('One number is less than 45')
else:
    print('One number is less than 45 is not true')
# Example


# 7
num_01 = int(input('Enter your number: '))
if -10 <= num_01 <= 0:
    print('Your number is in interval [-10:0]')
elif 2 <= num_01 <= 15:
    print('Your number is in interval [2:15]')
else:
    print('Your number is not in either interval')
# Example


# 8
a = int(input('Enter positive two digit number: '))
if a % 10 == 5 or a // 10 == 5:
    print('a has 5 in it')
else:
    print('a has no 5 in it')
# Example


# 9
L = input().split()
if len(L) == len(set(L)):
    print('All symbols are unique')
else:
    print('Not all symbols are unique')
# Example


# 10
number = int(input())
if str(number) == str(number)[::-1]:
    print('Number is palindrome')
else:
    print('Number is not palindrome')
# Example


# 11
a, b = 0, []
if a and b:
    print("Both variables are 'True'")
    print(a, b)
elif a or b:
    print("One of variables is 'True'")
    print(a or b)
else:
    print("Both variables are 'False'")
# Example


# 12
print(not any(map(int, input().split())))
# Example

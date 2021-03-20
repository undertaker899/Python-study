# Example
print(round(3.14159**2/2))
# Function (round)

# Example
numbers = input()
numbers_split = numbers.split()
numbers_joined = '\n'.join(numbers_split)
print(numbers_joined)
# Methods .split and .join

# Example
hours = 16
minutes = 9
seconds = 5
print("%02d:%02d:%02d" % (hours, minutes, seconds))
# String Formatting

# Example
L1 = ["a", "b", "c", 1, 2, 3, 4]
print(L1[1:4])

L2 = ["a", "b", "c", 1, 2, 3, 4]
print(L2[::3])

L3 = ["a", "b", "c", 1, 2, 3, 4]
print(L3[3::-1])

L4 = ["a", "b", "c", 1, 2, 3, 4]
print(L4[:3:-1])
#  Slices

# Example
letters = ['a', 'b', 'c', 'd']
print(letters)
letters.append('e')
print(letters)
letters.pop(3)
print(letters)
# Methods .append and .pop

# Example
L = [3.3, 4.4, 5.5, 6.6]
print(list(map(round, L)))

L = ['3.3', '4.4', '5.5', '6.6']
print(list(map(float, L)))
# Function (map)

# Example
string = input()
list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
print(sum(list_of_numbers[::3]))
# Method .split, function (map), slices

# Example
list_of_numbers = list(map(int, input().split()))
list_of_numbers = list_of_numbers[::-1]
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)
# Function (map), method .split and .append, slices

# Example
book = input("Book:")
author_name = input("Author name:")
publication_date = input("Publication date:")
d = {'book': book, 'author': author_name, 'year': publication_date}
print(d)
# Dictionary

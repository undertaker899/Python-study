# 1
print(round(3.14159 ** 2 / 2))
# Example


# 2
numbers = input()
numbers_split = numbers.split()
numbers_joined = '\n'.join(numbers_split)
print(numbers_joined)
# Example


# 3
print("%02d:%02d:%02d" % (int(input('Enter hours: ')), int(input('Enter minutes: ')), int(input('Enter seconds: '))))
# Example


# 4
L = ["a", "b", "c", 1, 2, 3, 4]
print(L[1:4])
print(L[::3])
print(L[3::-1])
print(L[:3:-1])
#  Example


# 5
letters = ['a', 'b', 'c', 'd']
print(letters)
letters.append('e')
print(letters)
letters.pop(0)
print(letters)
# Example


# 6
L = [3.3, 4.4, 5.5, 6.6]
print(list(map(round, L)))

L = ['3.3', '4.4', '5.5', '6.6']
print(list(map(float, L)))
# Example


# 7
string = input()
list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
print(sum(list_of_numbers[::3]))
# Example


# 8
list_of_numbers = list(map(int, input().split()))
list_of_numbers = list_of_numbers[::-1]
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)
# Example


# 9
print({'book': input("Book:"), 'author': input("Author name:"), 'year': input("Publication date:")})
# Example


# 10
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
shopping_center[-1].append("Uniqlo")
print(shopping_center)
# Example


# 11
print('Number of unique symbols: ', len(set(input('Enter your text: '))))
# Example


# 12
first_str, second_str = input("Enter fist string: "), input("Enter second string: ")
print(set(first_str).symmetric_difference(set(second_str)))
# Example

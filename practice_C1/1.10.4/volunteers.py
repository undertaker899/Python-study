class People:
    def __init__(self, name, location, status):
        self.name = name
        self.location = location
        self.status = status


class Person(People):
    def get_person(self):
        return f'''{self.name}, {self.location}, status "{self.status}"'''


ivan = Person('Ivan Petrov', 'Moscow', 'Mentor')
karina = Person('Karina Smirnova', 'Saint-Petersburg', 'Student')
volunteers = [ivan, karina]
for i in volunteers:
    print(i.get_person())

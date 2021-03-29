class People:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Role(People):
    def __init__(self, name, location, status):
        super().__init__(name, location)
        self.status = status


ivan = Role('Ivan Petrov', 'Moscow', 'Mentor')
karina = Role('Karina Smirnova', 'Saint-Petersburg', 'Student')
volunteers = [ivan, karina]
for i in volunteers:
    print(f'''{i.name}, {i.location}, status "{i.status}"''')

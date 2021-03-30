class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def get_person(self):
        return f'''Client: "{self.name}". Balance: {self.balance}'''


ivan = Client('Ivan Petrov', 50)
marina = Client('Marina Petrova', 270)
oleg = Client('Oleg Tarasov', 900)
clients = [ivan, marina, oleg]
for i in clients:
    print(i.get_person())

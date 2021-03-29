class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


ivan = Client('Ivan Petrov', 50)
marina = Client('Marina Petrova', 270)
oleg = Client('Oleg Tarasov', 900)
clients = [ivan, marina, oleg]
for i in clients:
    print(f"""Client: "{i.name}". Balance: {i.balance} rub.""")

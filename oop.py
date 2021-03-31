# 1
import datetime


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


peter = User(email="peterrobertson@mail.com", name="Peter Robertson")
julia = User("Julia Donaldson", "juliadonaldson@mail.com")


class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Product("eggs", "food", 5)
# Example


# 2
class Event:
    def __init__(self, timestamp=0, event_type='', session_id=''):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]


for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(1549461608000, "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", 6)
    test_view_event.show_description()
    print(test_view_event.type)
# Example


# 3
class Square:
    def __init__(self, side):
        self.side = side


class SquareFactory:

    @staticmethod
    def square_side(side):
        return Square(side)


square_01 = SquareFactory.square_side(4)
print(square_01.side)
# Example


# 4
class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 120
print(jane.happiness)
# Example


# 5
class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


ParentClass.method(0)
ParentClass.call_original_method()

ChildClass.method(0)
ChildClass.call_original_method()

my_obj = ParentClass()
my_obj.method(1)
my_obj.call_class_method()
# Example


# 6
class Squares:
    _side = None

    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value

    @property
    def get_area(self):
        return self.side ** 2


sq1 = Squares(1)
sq1.side = 2
print(sq1.side)
# Example

class Ticket:
    def __init__(self, name, base_price):
        self.__name = name
        self.base_price = base_price

    def get_name(self):
        return self.__name

    def price(self):
        return self.base_price


class StudentTicket(Ticket):
    def price(self):
        return super().price() * 0.5


class GroupTicket(Ticket):
    def __init__(self, name, base_price, people):
        super().__init__(name, base_price)
        self.__people = people

    def price(self):
        return super().price() * self.__people * 0.8

student = StudentTicket("Museum", 200)
group = GroupTicket("Zoo", 300, 4)
print (student.get_name(),group.price())

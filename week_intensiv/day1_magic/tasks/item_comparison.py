class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        try:
            return self.name == other.name and self.price == other.price
        except AttributeError:
            return False
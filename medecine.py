class medecine :


    def __init__(self, name, shelf, price):
        self.name = name
        self.shelf = shelf
        self.price = price

    def place(self):
        return '{} is in {}'.format(self.name, self.shelf)

    def price(self):
        return self.price

    def __repr__(self):
        return "Medecine ('{}', '{}', {})".format(self.name, self.shelf, self.price)
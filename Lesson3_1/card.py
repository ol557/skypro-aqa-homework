class Card:
    number = "0000 0000 0000"
    validDate = "12/2025"
    holder = "unknown"

    def __init__(self, number, date, holder):
        self.number = number
        self.validDate = date
        self.holder = holder


    def pay(self, amount):
        print("С карты", self.number, "списано", amount)
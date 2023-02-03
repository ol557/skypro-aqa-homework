class Smartphone:
    def __init__(self, stamp, model, number):
        self.stamp = stamp
        self.model = model
        self.number = number

    def printer(self):
        print(str(self.stamp), str(self.model), str(self.number))

    def sayModel(self):
        print("Модель", self.model)

    def sayNumber(self):
        print("Номер", self.number)

    def sayStamp(self):
        print("Марка", self.stamp)

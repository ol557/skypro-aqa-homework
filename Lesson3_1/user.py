class User:
    age = 0
    
    def __init__(self, name):
        print("а вот и я")
        self.username = name

    def sayName(self):
        print("Меня зовут",self.username)

    def sayAge(self):
        print("Мне",self.age,"лет")

    def setAge (self, newAge):
        self.age = newAge
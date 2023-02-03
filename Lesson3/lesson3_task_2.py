from smartphone import Smartphone

smartphone1 = Smartphone("iPhone", "5", "+7911")
smartphone2 = Smartphone("iPhone", "5S", "+7922")
smartphone3 = Smartphone("iPhone", "8", "+7933")
smartphone4 = Smartphone("iPhone", "8+", "+7944")
smartphone5 = Smartphone("iPhone", "x", "+7955")


catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for i in catalog:
    i.printer()

smartphone1.sayModel()
smartphone1.sayNumber()
smartphone5.sayStamp()
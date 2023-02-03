from user import User
from card import Card

Alex = User("Alex")


Alex.sayName()
Alex.setAge(33)
Alex.sayAge()

card = Card ("1234 5678 4321", "28/2028", "Alex S")

card.pay(1000)
from address import Address
from address import Mailing

mailing1 = Mailing(to=Address("123456", "Moscow", "Lenina", "1", "21"), 
from_=Address("654321", "Ufa", "Mira", "24", "8"), 
cost=500, track="ADC123") 

print("Отправление", mailing1.track, 
"из", mailing1.to.city, mailing1.to.street, mailing1.to.house, mailing1.to.apartment,
"в", mailing1.from_.city, mailing1.from_.street, mailing1.from_.house, mailing1.from_.apartment, 
"стоимость", mailing1.cost, "рублей")



#mailingTo = Address (11111, "Mos", "Len", 1, 24)
#mailingFrom = Address(22222, "Vld", "Kir", 2, 25)
#mailing1 = Mailing(mailingTo, mailingFrom, 1000, "big")


#def printer(self):
        #print(str(self.to), str(self.frome), str(self.track))

#print(self.to, str(self.frome), str(self.track))
class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

class Mailing:
    def __init__(self, to, from_, cost, track):
        self.to = to 
        #to = Address
        self.from_ = from_ 
        #frome = Address
        self.cost = cost
        self.track = track
        

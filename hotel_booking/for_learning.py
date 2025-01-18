import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})


class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel and change its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
    
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)
        

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for booking reservation!
        Here is your booking data:
        Name: {self.the_customer_name}
        Hotel Name:{self.hotel.name}
        """
        return content
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2

# Instance variables
# hotel_id and name are instance variables
hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name, "\n", hotel2.name)

# class variables
# watermark is a class variable
print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)

# Instance method
print(hotel1.available())

# class method
# classmethod decorator @classmethod is used
# cls parameter is used instead of self
print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

# Instance variables and instance methods are instance attributes
# class variables and class methods are class attributes

# property
# It is a method which behaves like a variable
ticket1 = ReservationTicket(customer_name="     steve smith   ", hotel_object=hotel1)
print(ticket1.generate())
print(ticket1.the_customer_name)

# static method
# @staticmethod decorator is used
converted = ReservationTicket.convert(10)
print(converted)




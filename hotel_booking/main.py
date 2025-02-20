import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
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
        
class Spa_Hotel(Hotel):
    def book_spa_package(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for booking reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel Name:{self.hotel.name}
        """
        return content

class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel Name:{self.hotel.name}
        """
        return content

    
class CreditCard:
    def __init__(self, number):
        self.number = number
        
    
    def validate(self, expiration, holder, cvc):
        credit_data = {"number": self.number, "expiration": expiration,
                       "holder": holder, "cvc": cvc}
        if credit_data in df_cards:
            return True

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == str(self.number), 
                                         "password"].squeeze()
        if password == given_password:
            return True
        

print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Spa_Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234657890123456")
    if credit_card.validate(expiration="12/26", holder="RAJU SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
            print(reservation_ticket.generate())

            spa_booking = input("Do you want to book a spa package? ")
            if spa_booking == "yes":
                spa_reservation_ticket = SpaReservationTicket(customer_name=name,
                hotel_object=hotel)
                print(spa_reservation_ticket.generate())

        else:
            print("Credit Card authentication failed!")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free")
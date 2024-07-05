import pandas as pd

df = pd.read_csv("hotels.csv", dtype = {"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Books the hotel and changes the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "yes"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        """Checks the availability of the hotel"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class TicketConfirmation:
    def __init__(self, customer_name,hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_name
    def generate(self):
        content = f"""
        Thank you for your booking our hotel!
        here are your booking details:
        Name:{self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")

    TicketConfirmation = TicketConfirmation(customer_name=name, hotel_name=hotel)
    print(TicketConfirmation.generate())

else:
    print("Hotel is not available.")
#Import pandas
import pandas as pd

#Load the datasets
df = pd.read_csv("hotels.csv", dtype={"id": str})

#Create class Hotel and define the functions
class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Books the hotel and changes the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)
    def available(self):
        """Checks the availability of the hotel"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # "@" is used for declaring decorator.
    #Class Method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    #Magic Methods
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False

#Create class TicketConfirmation and define the functions
class TicketConfirmation:
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_name
    def generate(self):
        content = f"""
        Thank you for booking our hotel!
        Here are your booking details:
        Name:{self.get_customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content

    #Property
    @property
    def get_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    #Static Method
    @staticmethod
    def convert(amount):
        return amount * 1.6

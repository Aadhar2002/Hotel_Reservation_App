#Import pandas
import pandas as pd

#Load the datasets
df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)

#Create class Hotel and define the functions
class Hotel:
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

#Create class TicketConfirmation and define the functions
class TicketConfirmation:
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_name
    def generate(self):
        content = f"""
        Thank you for booking our hotel!
        Here are your booking details:
        Name:{self.customer_name}
        Hotel Name: {self.hotel.name}
        Check-in Date: {check_in_date}
        Check-out Date: {check_out_date}
        """
        return content

#Create the class CreditCard to get the credit card details
class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False

#Create the class SecurePayment to authenticate the credit card and the payment.
class SecurePayment(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

#Print the dataframe
print(df)

#Enter the hotel id
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

#Enter the check in and check out dates
check_in_date = input("Enter the check in date of your stay: ")
check_out_date = input("Enter the check out date of your stay: ")

#Check if the hotel is available
if hotel.available():

    #Validate and authenticate the credit card for payment
    credit_card = SecurePayment(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        user_password = input("Enter the user password: ")
        if credit_card.authenticate(given_password = user_password):

            #Book the hotel and give the confirmation ticket
            hotel.book()
            name = input("Enter your name: ")
            TicketConfirmation = TicketConfirmation(customer_name=name, hotel_name=hotel)
            print(TicketConfirmation.generate())
        else:
            print("Authentication Failed.")
    else:
        print("There was a problem with your payment")

else:
    print("Hotel is not available.")
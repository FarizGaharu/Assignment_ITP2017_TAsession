import random
class Booking:
    def __init__(self):
        pass
    def check_availability(self,**kwargs):
        booking_type = kwargs['booking_type']
        booking_class =kwargs['booking_class']
        if booking_type == "Railways":
            railways = kwargs ["railways"]
            if railways.Railways_Seats[booking_class] != 0 :
                print("Train Is Available\n")
                return True
            else:
                print("Train Is Not Available\n")
                return False

    def makeReservation(self,**kwargs):
        booking_type = kwargs['booking_type']
        customer = kwargs['customer']
        availability_status = kwargs['availability_status']
        if (availability_status == True) and (booking_type == "Railways"):
            booking_class = kwargs['booking_class']
            railways= kwargs['railways']
            railways.Railways_SeatsS[booking_class] -= 1
            customer.customer_record['Wallet'] += railways.Railways_Seats[booking_class]
            customer.customer_record['Booking ID']['Railways'] = 'RAIL'+str(random.randrange(10,1000,2))

class Bookable(object):
    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, customer, booking_class):
        if self.is_available(booking_class):
            self.decrement_items(booking_class)
            customer.customer_record['Wallet'] += self.get_price(booking_class)
            customer.customer_record['Booking ID'][self.get_class_name()] = self.get_id_prefix() + str(random.randrange(10, 1000, 2))

    def get_class_name(self):
        return self.__class__.__name__

    def get_items(self, booking_class):
        raise NotImplementedError

    def get_price(self, booking_class):
        raise NotImplementedError

    def decrement_items(self, booking_class):
        raise NotImplementedError

    def get_id_prefix(self):
        raise NotImplementedError


class Railways(Bookable):
    CLASS_FIRST = 'First Class'
    CLASS_BUSINESS = 'Business Class'
    CLASS_PREMIUM_ECONOMY = 'Premium Economy'
    CLASS_ECONOMY = 'Regular Economy'

    def __init__(self, railways_n):
        super(Railways, self).__init__()
        self.railways_n = railways_n
        self.seats = {
            self.CLASS_FIRST: 50,
            self.CLASS_BUSINESS: 50,
            self.CLASS_PREMIUM_ECONOMY: 100,
            self.CLASS_ECONOMY: 150,
        }
        self.prices = {
            self.CLASS_FIRST: 3000000,
            self.CLASS_BUSINESS: 2000000,
            self.CLASS_PREMIUM_ECONOMY: 1000000,
            self.CLASS_ECONOMY: 500000,
        }

    def get_items(self, booking_class):
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return 'RAIL'

    def get_price(self, booking_class):
        return self.prices[booking_class]


    inp = input ("Categories of Class:\t\t\tPrice\n"
                "(1) First Class\t\t\t\t\t IDR %d\n"
                "(2) Business Class\t\t\t\t IDR %d\n"
                "(3) Premium Economy Class\t\t IDR %d\n"
                "(4) Economy Class\t\t\t\t IDR %d\n"
                "Please, input the name or the number: ")

    if inp == "First Class" or inp == "1":
         Class = Category1()
         out_type = "(1) First Class"
    elif inp == "Business Class" or inp == "2":
         Class = Category2()
         out_type = "(2) Business Class"
    elif inp == "Premium Economy Class" or inp == "3":
         Class = Category3()
         out_type = "(3) Premium Economy Class"
    elif inp == "Economy Class" or inp == "4":
         Class = Category4()
         out_type = "(4) Economy Class"
    else:
        print("Please, only input with the data of [Name] or [Number] that already listed"
                " in the [Categories of Class]")
        input("Press 'ENTER' to continue")


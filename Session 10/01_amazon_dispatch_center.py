#### Code to complete [START] ####

class Command():

    total_command = 0
    total_price = 0

    def __init__(self, id_buyer, id_item, quantity_item, price_item):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity_item = quantity_item
        self.price_item = price_item
        # Updating total price
        Command.total_price += self.get_price()
        # Updating total command 
        Command.total_command += 1
    
    def get_price(self):
        price = self.quantity_item * self.price_item
        return price
    
    def __str__(self):
        s = "{}, {} : {} * {} = {}".format(self.id_buyer, self.id_item, self.price_item, self.quantity_item, self.get_price())
        return s
    
    @classmethod
    def get_number_total_command(cls):
        return Command.total_command

    @classmethod
    def get_total_price(cls):
        return Command.total_price
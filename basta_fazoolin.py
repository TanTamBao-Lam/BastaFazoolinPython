import datetime


# Making the Menus
class Menu:
    # Constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # String representation: {Menu} is available from {start time} to {end time}
    def __repr__(self):
        return "{n} menu available from {st} to {et}".format(n=self.name, st=self.start_time, et=self.end_time)

    # Calculate total price based on the purchased items
    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            # if ordered item is in the menu, add its price to the total
            if item in self.items:
                total_price += self.items[item]

        return total_price


# Brunch menu.
brunch_menu = Menu("Brunch",
                   {
                       'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                       'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
                   },
                   11.00,
                   16.00)

# Early bird menu.
early_bird_menu = Menu("Early Bird",
                       {
                           'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                           'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                           'coffee': 1.50, 'espresso': 3.00,
                       },
                       15.00,
                       18.00)

# Dinner menu
dinner_menu = Menu("Dinner",
                   {
                       'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
                       'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
                       'coffee': 2.00, 'espresso': 3.00
                   },
                   17.00,
                   23.00)

# Kid menu
kid_menu = Menu("Kid",
                {
                    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
                },
                11.00,
                16.00)

# Test representation of Menu class
print(brunch_menu)

# Test calculate order method of menu class.
order1_price = brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"])
print(order1_price)

order2_price = early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print(order2_price)


# Creating Franchise
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Restaurant is located at {addr}".format(addr=self.address)

    # Return all menus available at the given time
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu.name)

        if len(available_menus) > 0:
            return "Menus is available at {} is/are: {}".format(time, available_menus)
        else:
            return "No menu is available at {}".format(time)


# Flagship store and new installment.
flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kid_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kid_menu])

# test available menu
print(flagship_store.available_menus(12.00))
print(new_installment.available_menus(17.00))


# Create Businesses
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# new menu Take a'Arepa
arepas_menu = Menu("Take a’ Arepa",
                   {
                        'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
                   },
                   10.00,
                   20.00)

# new franchise Take a' Arepa
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Basta Fazoolin' with my Heart business
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Take a' Arepa business
take_a_arepa = Business("Take a' Arepa", [arepas_place])

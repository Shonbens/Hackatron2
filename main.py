size_mappings = {
    1: "Small",
    2: "Large",
    3: "Extra Large",
    4: "Party Size"
}


cost_mappings = {
    "Small": 6,
    "Large": 10,
    "Extra Large": 12,
    "Party Size": 24
}



class Pizza():
    def __init__(self, size):
        self.size = size

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size()

    def get_cost(self):
        return cost_mappings[self.size]



class Order():
    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotal(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.get_cost()
        return total

# start processing the order
order = Order()


def run():
    print("\nWhat size pizza would you like?\n\n\
    _____________________________________________________________\n\
    | 1: Small  |  2: Large  |  3: Extra Large  |  4: Party Size |\n\
    |    $6     |     $10    |        $12       |       $24      |\n\
    |___________|____________|__________________|________________|\n\
    \n- Press 't' to choose your toppings\n")

    while True:
        try:

            response = input('-')

            if response == 't':
                break

            size_wanted = int(response)

            size_wanted = size_mappings[size_wanted]


            print(f"Pizza: {size_wanted}")
            order.addPizza(Pizza(size_wanted))
        except:
            print("An error occurred, please try again")
run()

print("your current order total: ", "$" + str(order.getTotal()))


topping_mappings = {
                    1: 'Anchovies',
                    2: 'Bacon',
                    3: 'Bell Peppers',
                    4: 'Black Olives',
                    5: 'Chicken',
                    6: 'Ground Beef',
                    7: 'Jalapenos',
                    8: 'Mushrooms',
                    9: 'Pepperoni',
                    10: 'Pineapple',
                    11: 'Spinach',
                    12: 'Onion'
                    }

topping_cost_mappings = {
                        'Anchovies': 1,
                        'Bacon': 1,
                        'Bell Peppers': 1,
                        'Black Olives': 1,
                        'Chicken': 1,
                        'Ground Beef': 1,
                        'Jalapenos': 1,
                        'Mushrooms': 1,
                        'Pepperoni': 1,
                        'Pineapple': 1,
                        'Spinach': 1,
                        'Onion': 1
                        }


class CustomerToppings():
    """ Have customer pick toppings for pizza"""

    def __init__(self, numToppings):
        self.numToppings = numToppings

    def set_toppings(self, numToppings):
        self.numToppings = numToppings

    def get_toppings(self):
        return topping_cost_mappings[self.numToppings]


class ToppingOrder():

    def __init__(self):
        self.topping = []

    def addTopping(self, toppings):
        self.topping.append(toppings)

    def toppingTotal(self):
        get_topping_total = 0
        for toppings in self.topping:
            get_topping_total += toppings.get_toppings()
        return get_topping_total

# Strat processing the order
topping_order = ToppingOrder()

def runTopping():
    print("\nWhat toppings would you like on your pizza?\n\n\
    ______________________________________________________________________\n\
    | 1: Anchovies |    2: Bacon    | 3: Bell Peppers |  4: Black Olives |\n\
    |  5: Chicken  | 6: Ground Beef |   7: Jalapenos  |   8: Mushrooms   |\n\
    | 9: Pepperoni |  10: Pineapple |   11: Spinach   |    12: Onions    |\n\
    |______________|________________|_________________|__________________|\n\
    Press 'f' for your final total: \n")

    while True:
        try:
            response = input('-')
            if response == 'f':
                break
            toppings_wanted = int(response)

            toppings_wanted = topping_mappings[toppings_wanted]

            print(f"Topping: {toppings_wanted}")
            topping_order.addTopping(CustomerToppings(toppings_wanted))
        except:
            print("An error occurred, please try again")

runTopping()

sub_size = int(order.getTotal())
sub_toppings =  int(topping_order.toppingTotal())
final_total = sub_size + sub_toppings

print(f" \nYour final total will be ${final_total}\n")
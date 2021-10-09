"""module that implement the restaurant and interaction with it
"""


class Person:
    """a class that implement a person

        Args:
            first_name (str): persons name
            last_name (str): persons surname
    """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        """getter for persons name
            Returns:
                str: persons name
        """
        return self._first_name

    def get_last_name(self):
        """getter for persons surname
            Returns:
                str: persons surname
        """
        return self._last_name


class Order:
    """a class that implement the order

        Args:
            order_list (list): names of dishes
    """
    def __init__(self, *order_list):
        self.order_list = list(order_list)

    def get_order_list(self):
        """getter for dishes
            Returns:
                list: dishes
        """
        return self.order_list

    def __str__(self):
        return str(self.order_list)


class Customer(Person):
    """a class that implement a customer

        Args:
            first_name (str): customers name
            last_name (str): customers surname
            address (str): customers address
            phone (str): customers phone
    """
    def __init__(self, first_name, last_name, address, phone):
        self._address = address
        self._phone = phone
        self._order = None
        super().__init__(first_name, last_name)

    def order_food(self, app, order, restaurant):
        """food ordering method

            Args:
                app (App): app from which the order will be
                order (Order): customers order
                restaurant (Restaurant): restaurant from which the order will be
        """
        self._order = order
        app.take_order(self, restaurant)

    def get_address(self):
        """getter for address:

            Returns:
                str: customers address
        """
        return self._address

    def get_order(self):
        """getter for order:

            Returns:
                str: customers order
        """
        return self._order


class App:
    """a class that implement the food ordering app
    """
    def __init__(self):
        self._delivers = []

    def take_order(self, customer, restaurant):
        """method for accepting an order from customer

            Args:
                customer (Customer): order customer
                restaurant (Restaurant): restaurant for ordering food
        """
        print(f'{customer.get_first_name()} order is accepted')
        self.transfer_order(restaurant, customer)

    def transfer_order(self, restaurant, customer):
        """method for transfering order to restaurant

            Args:
                restaurant (Restaurant): restaurant for ordering food
                customer (Customer): order customer
        """
        print(f'order transfered to {restaurant.get_name()}')
        restaurant.get_kitchen().prepare_order(customer.get_order())
        self.call_deliver(restaurant, customer)

    def call_deliver(self, restaurant, customer):
        """method for calling deliver

            Args:
                restaurant (Restaurant): restaurant for ordering food
                customer (Customer): order customer
        """
        print(f'calling deliver {self._delivers[-1].get_first_name()}')
        self._delivers[-1].deliver_order(customer.get_order(), customer.get_address(),
            restaurant.get_address())

    def add_deliver(self, deliver):
        """method for adding deliver in base

            Args:
                deliver (Deliver): deliver
        """
        self._delivers.append(deliver)


class Deliver(Person):
    """class that implement a deliver

        Args:
            first_name (str): delivers name
            last_name (str): delivers surname
    """
    def __init__(self, first_name, last_name,):
        super().__init__(first_name, last_name)
        self.state=None

    def deliver_order(self, order, customer_address, restaurant_address):
        """delivery method
        """
        print(f'order {order} is delivered from {restaurant_address} to {customer_address}')
        self.state='delivers'
        self.pay_off()

    def pay_off(self):
        """method that implement the calculation of the deliver and customer
        """
        self.state='free'
        print('customer paid')


class Client(Person):
    """class that implement a restaurant client

        Args:
            order (Order): food order
            first_name (str): client name
            last_name (str): client surname
            restaurant (Restaurant): the restaurant where the client is
    """
    def __init__(self, order, first_name, last_name, restaurant):
        self._restaurant = restaurant
        super().__init__(first_name, last_name)
        self._order = order

    def call_waiter(self, hall):
        """method for call the waiter

            Args:
                hall (Hall): the hall where the client is
        """
        print(f'{self._first_name} calling waiter')
        hall.get_waiters()[-1].take_order(self._order, self._restaurant)

    def pay_off(self, hall):
        """method to call the waiter for calculation

            Args:
                hall (Hall): he hall where the client is
        """
        hall.get_waiters()[-1].calculate_client(self._order)


class Waiter(Person):
    """class that implement a waiter

        Args:
            first_name (str): waiters name
            last_name (str): waiters surname
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def take_order(self, order, restaurant):
        """a method that implements the acceptance of an order by a waiter

            Args:
                oder (Order): dishes order
                resturant (Restaurant): the restaurant where the waiter works
        """
        print(f'accept the order: {order}')
        restaurant.get_kitchen().prepare_order(order)
        self.bring_order(order)

    def bring_order(self, order):
        """a method that implements the brought of an order by a waiter

            Args:
                order (Order): dishes order
        """
        print(f'{self.get_first_name()} brought the {order}')

    def calculate_client(self, order):
        """client calculation method

            Args:
                order (Order): dishes order
        """
        print(f'{self.get_first_name()} calculated {order}')


class Hall:
    """hall implementing class

        Args:
            free_places (int): free places in the hall
            hall (str): hall title
    """
    def __init__(self, free_places, title):
        self._title = title
        self._free_places = free_places
        self._waiters = []

    def add_waiter(self, waiter):
        """method of adding a waiter in the hall

            Args:
                waiter (Waiter): waiter
        """
        self._waiters.append(waiter)

    def get_waiters(self):
        """getter for waiters

            Returns:
            list: list of waiters in this hall
        """
        return self._waiters


class Kitchen:
    """kitchen implementing class

        Args:
            chef (Person): chef
            team (Person): chefs team
    """
    def __init__(self, chef, *team):
        self._chef = chef
        self._team = list(team)

    def prepare_order(self, order):
        """method for preparing an order

            Args:
                order (Order): dishes order
        """
        print(f'{order} is cooking')

    def add_cook(self, first_name, last_name):
        """method of adding a cook in the kitchen

            Args:
                first_name (str): cooks name
                last_name (str): cooks surname
        """
        self._team.append(Person(first_name, last_name))


class Restaurant:
    """class that implement the resturant

        Arggs:
            name (str): restaurant name
            address (str): restaurnt address
            working_hours (str): restaurant working hours
            chef (Person): chief-cooker
            team (Rerson): chiefs team
    """
    def __init__(self, name, address, working_hours, chef, *team):
        self._name = name
        self._working_hours = working_hours
        self._address = address
        self._kitchen = Kitchen(chef, team)
        self._halls = []

    def add_hall(self, hall):
        """method of adding a hall to a restaurant

            Args:
                hall (Hall): hall
        """
        self._halls.append(hall)

    def get_address(self):
        """getter for restaurant address

            Returns:
                str: restaurant address
        """
        return self._address

    def get_kitchen(self):
        """getter for restaurant kitchen

            Returns:
                Kitchen: restaurant kitchen
        """
        return self._kitchen

    def get_halls(self):
        """getter for restaurant halls

            Returns:
                list: restaurant halls
        """
        return self._halls

    def get_name(self):
        """getter for restaurant name

            Returns:
                str: restaurant name
        """
        return self._name


print('Customer:')
orderer = Customer('lesha', 'pavlov', 'tselinogradskaya, 58', '0668091721')
claude_monet = Restaurant('claude monet', 'sumskaya, 10', '08:00-20:00',
    Person('victor', 'barinov'), Person('maxim', 'lavrov'), Person('senya', 'chuhanin'))
glovo = App()
glovo.add_deliver(Deliver('sasha', 'ivanov'))
orderer.order_food(glovo, Order('pizza', 'sushi'), claude_monet)

print('Client:')
claude_monet.add_hall(Hall(10, 'red'))
claude_monet.get_halls()[-1].add_waiter(Waiter('nastya', 'fomina'))
client = Client(Order('borsch'), 'dima', 'nagiev', claude_monet)
client.call_waiter(claude_monet.get_halls()[-1])
client.pay_off(claude_monet.get_halls()[-1])

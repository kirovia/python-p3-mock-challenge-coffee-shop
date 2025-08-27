class Coffee:
    def __init__(self, name, all_orders = None, all_customers = None):
        self.name = name
        self.all_orders = []
        self.all_customers = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            return
        elif type(name) in [str] and len(name) >= 3:
            self._name = name
        else:
            raise ValueError('Name must be a string 3 characters or more in length')

    def orders(self):
        return self.all_orders
    
    def customers(self):
        return self.all_customers
    
    def num_orders(self):
        return len(self.all_orders)
    
    def average_price(self):
        all_prices = [order.price for order in self.all_orders]
        return sum(all_prices) / len(all_prices)

class Customer:
    def __init__(self, name, all_orders = None, all_coffees = None):
        self.name = name
        self.all_orders = []
        self.all_coffees = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) in [str] and len(name) in range(1, 15, 1):
            self._name = name
        else:
            raise ValueError('Name must be a string between 1-15 characters')
        
    def orders(self):
        return self.all_orders
    
    def coffees(self):
        return self.all_coffees
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        coffee.all_orders.append(self)
        if customer not in coffee.all_customers:
            coffee.all_customers.append(customer)
        customer.all_orders.append(self)
        if coffee not in customer.all_coffees:
            customer.all_coffees.append(coffee)
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError('Customer must be an instance of the Customer class')
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError('Coffee must be an instance of the Coffee class')
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            return
        elif type(price) in [float] and price > 1.0 and price < 10.0:
            self._price = price
        else:
            raise ValueError('Price must be a float between 1.0 and 10.0')
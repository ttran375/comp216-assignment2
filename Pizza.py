class Pizza:
    # Prices for different sizes
    size_prices = {"small": 6.99, "medium": 8.99, "large": 11.49, "x-large": 15.49}

    # Price per topping
    topping_price = 1.00

    def __init__(self, size="medium", toppings=None):
        self._size = size
        self.toppings = toppings if toppings else ["cheese"]

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in self.size_prices:
            raise ValueError(f"ERROR: {value} is not a valid size for a pizza")
        self._size = value

    def add(self, toppings):
        self.toppings.extend(toppings)

    def __str__(self):
        # Calculate the base price of the pizza
        base_price = self.size_prices[self._size]
        # Calculate the total price including toppings
        total_price = base_price + len(self.toppings) * self.topping_price
        return f"{self._size} pizza with {self.toppings} for ${total_price:.2f}"

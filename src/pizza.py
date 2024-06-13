class Pizza:
    valid_sizes = ["small", "medium", "large", "x-large"]
    prices = {"small": 6.49, "medium": 8.49, "large": 10.49, "x-large": 13.49}

    def __init__(self, size="medium", toppings=None):
        self.__size = size
        self.__toppings = toppings if toppings is not None else ["cheese"]
        self.size = size  # This will use the size property setter to validate size

    @property
    def price(self):
        base_price = self.prices[self.__size]
        additional_toppings_cost = 0.50 * len(self.__toppings)
        return base_price + additional_toppings_cost

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value not in self.valid_sizes:
            raise ValueError(f"ERROR: {value} is not a valid size for a pizza")
        self.__size = value

    def add(self, toppings):
        self.__toppings.extend(toppings)

    def __str__(self):
        return f"{self.__size} pizza with {self.__toppings} for ${self.price:.2f}"


# Test harness
if __name__ == "__main__":
    print(f"Creating a default pizza")
    p = Pizza()
    print(p)

    toppings = "cheese olive".split()
    print(f"\nAdding topping: {toppings}")
    p.add(toppings=toppings)
    print(p)

    print(f"\nCreating a new pizza")
    p = Pizza("large", "cheese pepper".split())
    print(p)

    toppings = ["pineapple", "mushroom"]
    print(f"\nAdding topping: {toppings}")
    p.add(toppings)
    print(p)

    size = "x-large"
    p.size = size
    print(f"\nChanging order size to {size}")
    print(p)

    size = "gigantic"
    print(f"\nChanging order size to {size}")
    try:
        p.size = size
    except ValueError as err:
        print(err)

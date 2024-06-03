class TransactionHistory:
    def __init__(self):
        self.part_numbers = []
        self.part_descs = []
        self.part_prices = []
        self.part_errors = []

    def add_history(self, part_number, desc, price, err):
        self.part_numbers.append(part_number)
        self.part_descs.append(desc)
        self.part_prices.append(price)
        self.part_errors.append(err)

    def print_history(self):
        for i in range(len(self.part_numbers)):
            print()
            print(f"Transaction Number: {i+1}")
            print(f"Part Number: {self.part_numbers[i]}")
            print(f"Part Desc: {self.part_descs[i]}")
            print(f"Part Prices: {self.part_prices[i]}")
            print(f"Part Error: {self.part_errors[i]}")
            print()

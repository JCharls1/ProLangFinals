import transaction_history

class PartInventory:
    def __init__(self):
        self.numbers_and_descs = {}
        self.prices = {}
        self.history = transaction_history.TransactionHistory()

    def add_part(self):
        try:
            part_number = int(input("Enter the Part Number: "))
        except ValueError:
            print("Transaction with error recorded and ceased.")
            self.history.add_history(0, "Adding part number", 0, "Invalid input for part number")
            return

        desc = input("Enter the Part Description: ")
        self.numbers_and_descs[part_number] = desc

        try:
            part_price = float(input("Enter the Part Price: "))
        except ValueError:
            print("Transaction with error recorded and ceased.")
            self.history.add_history(part_number, "Adding part price", 0, "Invalid input for part price")
            return

        self.prices[part_number] = part_price

        print("\nAdded to the Parts Inventory:")
        print(f"Part Number: {part_number}")
        print(f"Part Description: {self.numbers_and_descs[part_number]}")
        print(f"Part Price: {self.prices[part_number]}")
        print("Transaction without error recorded.")
        self.history.add_history(part_number, self.numbers_and_descs[part_number], self.prices[part_number], "No Error")

    def access_parts(self):
        part_number = int(input("Enter the Part Number of the part that you wanted to see: "))
        print(f"The part that has the Part Number: {part_number}")
        print(f"Part Description: {self.numbers_and_descs.get(part_number)}")
        print(f"Part Price: {self.prices.get(part_number)}\n")

    def update_parts(self):
        try:
            part_number = int(input("Enter the part number of the part you want to update: "))
        except ValueError:
            print("Transaction with error recorded and ceased.")
            self.history.add_history(0, "Picking a part number to update", 0, "Invalid input for part number")
            return

        new_description = input("Enter the updated Description for the part: ")

        try:
            new_price = float(input("Enter updated price for the part: "))
        except ValueError:
            print("Transaction with error recorded and ceased.")
            self.history.add_history(part_number, "Picking a part price to update", 0, "Invalid input for part price")
            return

        print(f"Here's the updated Description and Price for part number {part_number}")
        print(f"Old Description: {self.numbers_and_descs.get(part_number)}")
        self.numbers_and_descs[part_number] = new_description
        print(f"New Description: {self.numbers_and_descs[part_number]}\n")

        print(f"Old Price {self.prices.get(part_number)}")
        self.prices[part_number] = new_price
        print(f"New Price: {self.prices[part_number]}")
        print("Transaction without error recorded.")
        self.history.add_history(part_number, self.numbers_and_descs[part_number], self.prices[part_number], "No Error")
        print()

    def delete_part(self):
        part_number = int(input("Enter the part number you want to delete: "))
        if part_number in self.numbers_and_descs and part_number in self.prices:
            del self.numbers_and_descs[part_number]
            del self.prices[part_number]
            print(f"Deleted part from the inventory {part_number}")
            self.history.add_history(part_number, "Picking a part number to delete", 0, "No Error")
        else:
            print("Transaction with error recorded and ceased.")
            self.history.add_history(0, "Picking a part number to delete", 0, "Invalid input for part number")

    def print_log(self):
        self.history.print_history()

    def input_error(self):
        print("Transaction with error recorded.")
        self.history.add_history(0, "Wrong input for transaction", 0, "Wrong input for transaction")

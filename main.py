import part_inventory
import transaction_history

class Main:
    def run(self):
        inventory = part_inventory.PartInventory()
        while True:
            print("Choose action:")
            print("A. Add part")
            print("B. Change part")
            print("C. Delete a part")
            print("D. Print Transactions")
            print("E. Access Parts")
            print("X. Exit")
            choice = input("Enter choice: ")

            if len(choice) > 1:
                inventory.input_error()
            elif choice.lower() == 'a':
                inventory.add_part()
                inventory.print_log()
            elif choice.lower() == 'b':
                inventory.update_parts()
                print()
            elif choice.lower() == 'c':
                inventory.delete_part()
                print()
            elif choice.lower() == 'd':
                inventory.print_log()
            elif choice.lower() == 'e':
                inventory.access_parts()
                print()
            elif choice.lower() == 'x':
                break

if __name__ == "__main__":
    Main().run()

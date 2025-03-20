import sys
from colorama import Fore, Style
from store import Store
from products import Product

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = Store(product_list)


def start(Store):
    """
    Starts the interactive store menu where users can perform various actions such as:
    - Listing all products in the store
    - Displaying the total amount of products in the store
    - Making an order
    The function continuously prompts the user for input until they choose to quit.
    :param Store: The store object that manages the products and their interactions.
    :type Store: Store
    :return: None
    """
    shopping_list = []

    while True:
        print("\n           Store Menu          ")
        print("\n          ------------         ")
        print(Fore.GREEN + "1. " + Style.RESET_ALL + "List all products in store")
        print(Fore.GREEN + "2. " + Style.RESET_ALL + "Show total amount in store")
        print(Fore.GREEN + "3. " + Style.RESET_ALL + "Make an order")
        print(Fore.GREEN + "4. " + Style.RESET_ALL + "Quit")

        user_choice = input("\nEnter your choice: ")

        if user_choice == "1":
            products = best_buy.get_all_products()
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.name} - Price: {product.price}, Quantity: {product.quantity}")

        elif user_choice == "2":
            print(f"\nTotal quantity in store: {best_buy.get_total_quantity()}")

        elif user_choice == "3":
            while True:
                print("\nAvailable Products:")
                for index, product in enumerate(best_buy.get_all_products(), start=1):
                    print(f"{index}. {product.name} - Price: {product.price}, Quantity: {product.quantity}")

                product_choice = input("\nWhen you want to finish order, enter empty text.\nWhich product # do you want? ")

                if not product_choice:
                    break

                try:
                    product_index = int(product_choice) - 1
                    product = best_buy.get_all_products()[product_index]
                except (ValueError, IndexError):
                    print(Fore.RED + "\nInvalid product number. Please try again." + Style.RESET_ALL)
                    continue

                quantity = input(f"\nWhat amount do you want? ")

                try:
                    quantity = int(quantity)
                except ValueError:
                    print(Fore.RED + "\nPlease enter a valid quantity." + Style.RESET_ALL)
                    continue

                if quantity <= 0:
                    print(Fore.RED + "\nQuantity must be greater than zero. Please try again." + Style.RESET_ALL)
                    continue

                shopping_list.append((product, quantity))
                print(f"\nProduct added to list: {product.name} (x{quantity})")

            total_price = best_buy.order(shopping_list)
            print(f"\nTotal price of the order: {total_price}")

        elif user_choice == "4":
            print("\nBye!")
            sys.exit()

        else:
            print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        start(Store)
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram terminated by user." + Style.RESET_ALL)
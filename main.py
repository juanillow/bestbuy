import products
import store


def start(best_buy):
    """Start a simple store menu"""
    while True:
        print("\n   Store Menu")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = input("Please choose a number: ")
        except EOFError:
            print("\nGoodbye!")
            break

        if choice == "1":
            active_products = best_buy.get_all_products()
            for index, product in enumerate(active_products, start=1):
                print(f"{index}. ", end="")
                product.show()
        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        elif choice == "3":
            active_products = best_buy.get_all_products()

            if len(active_products) == 0:
                print("There are no active products to order.")
                continue

            print("\nAvailable products:")
            for index, product in enumerate(active_products, start=1):
                print(f"{index}. ", end="")
                product.show()

            print("Press Enter without typing a number to finish your order.")
            shopping_list = []

            while True:
                product_choice = input("Product number: ")
                if product_choice == "":
                    break

                if not product_choice.isdigit():
                    print("Invalid product number.")
                    continue

                product_index = int(product_choice)
                if product_index < 1 or product_index > len(active_products):
                    print("Product number out of range.")
                    continue

                quantity_choice = input("Quantity: ")
                if not quantity_choice.isdigit() or int(quantity_choice) <= 0:
                    print("Invalid quantity.")
                    continue

                shopping_list.append(
                    (active_products[product_index - 1], int(quantity_choice))
                )

            if len(shopping_list) == 0:
                print("No products selected.")
                continue

            try:
                total_price = best_buy.order(shopping_list)
                print(f"Order made! Total payment: {total_price}")
            except Exception as e:
                print(f"Order failed: {e}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def main():
    """Create default inventory and start the UI"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

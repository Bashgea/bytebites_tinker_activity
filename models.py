'''
1. Customer
- Represents a single ByteBites customer.
- Stores the customer's name and a unique identifier (id).
- Tracks the customer's past purchase history so the system can verify they are real users.
- Purchase history should be represented as a collection (list/array) of Transaction objects.

2. Item (or FoodItem)
- For each item, we must track:
  - name
  - price
  - category (for example, "Drinks", "Desserts", "Burgers")
  - popularity rating (for example, a numeric score)

3. ItemCatalog (or Menu)
- Represents the full collection of items that ByteBites offers.
- Internally stores a collection (list/array) of Item objects.
- Provides functionality to:
  - add items to the catalog
  - retrieve all items
  - filter items by category (for example, return all "Drinks" or all "Desserts").

4. Transaction (or Order)
- Represents a single purchase made by a customer.
- Stores the collection of Item objects that the customer selected.
- Computes the total cost of the transaction by summing the prices of all items.
- Can optionally reference the Customer who made the purchase.

'''


class Item:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class ItemCatalog:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def get_all_items(self) -> list[Item]:
        return list(self.items)

    def filter_by_category(self, category: str) -> list[Item]:
        return [item for item in self.items if item.category == category]

    def get_items_sorted_by_price(self, desc: bool = False) -> list[Item]:
        return sorted(self.items, key=lambda item: item.price, reverse=desc)

    def get_items_sorted_by_popularity(self, desc: bool = True) -> list[Item]:
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=desc)


class Transaction:
    def __init__(self, items: list[Item], customer=None):
        self.items = items
        self.customer = customer

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.purchase_history: list[Transaction] = []

    def get_purchase_history(self) -> list[Transaction]:
        return self.purchase_history

    def get_total_spent(self) -> float:
        return sum(transaction.compute_total() for transaction in self.purchase_history)


if __name__ == "__main__":
    # --- Build catalog ---
    catalog = ItemCatalog()
    catalog.add_item(Item("Cheeseburger",   8.99,  "Burgers",  4.5))
    catalog.add_item(Item("Veggie Burger",  7.49,  "Burgers",  3.8))
    catalog.add_item(Item("Lemonade",       2.99,  "Drinks",   4.7))
    catalog.add_item(Item("Iced Coffee",    3.49,  "Drinks",   4.2))
    catalog.add_item(Item("Chocolate Cake", 5.99,  "Desserts", 4.9))
    catalog.add_item(Item("Brownie",        3.99,  "Desserts", 4.1))

    # --- Filter by category ---
    print("=== Drinks ===")
    for item in catalog.filter_by_category("Drinks"):
        print(f"  {item.name}: ${item.price}")

    # --- Sort by price (ascending) ---
    print("\n=== Menu by Price (low to high) ===")
    for item in catalog.get_items_sorted_by_price(desc=False):
        print(f"  {item.name}: ${item.price}")

    # --- Sort by popularity (descending) ---
    print("\n=== Menu by Popularity (high to low) ===")
    for item in catalog.get_items_sorted_by_popularity():
        print(f"  {item.name}: {item.popularity_rating}")

    # --- Place an order ---
    customer = Customer(id=1, name="Alice")
    order_items = [
        catalog.filter_by_category("Burgers")[0],  # Cheeseburger
        catalog.filter_by_category("Drinks")[0],   # Lemonade
        catalog.filter_by_category("Desserts")[0], # Chocolate Cake
    ]
    transaction = Transaction(items=order_items, customer=customer)
    customer.purchase_history.append(transaction)

    print(f"\n=== Order for {customer.name} ===")
    for item in transaction.items:
        print(f"  {item.name}: ${item.price}")
    print(f"  Order total:  ${transaction.compute_total():.2f}")
    print(f"  Total spent:  ${customer.get_total_spent():.2f}")

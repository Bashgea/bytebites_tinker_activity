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
        return self.items

    def filter_by_category(self, category: str) -> list[Item]:
        return [item for item in self.items if item.category == category]


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

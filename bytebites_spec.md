Client Feature Request
CANDIDATE CLASSES

We need to design the core backend data model for the ByteBites app using a small set of classes.

1. Customer
- Represents a single ByteBites customer.
- Stores the customer's name and a unique identifier (id).
- Tracks the customer's past purchase history so the system can verify they are real users.
- Purchase history should be represented as a collection (list/array) of Transaction objects.

2. Item (or FoodItem)
- Represents a single food or drink that ByteBites sells (for example, "Spicy Burger" or "Large Soda").
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

Your implementation should create these candidate classes (or equivalent names) and ensure the relationships between them match the descriptions above.
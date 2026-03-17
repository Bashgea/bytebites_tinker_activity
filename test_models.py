from models import Item, ItemCatalog, Transaction, Customer

# --- Items ---
burger = Item("Spicy Burger", 8.99, "Burgers", 4.5)
soda = Item("Large Soda", 2.49, "Drinks", 3.8)
brownie = Item("Chocolate Brownie", 3.99, "Desserts", 4.9)
water = Item("Bottled Water", 1.49, "Drinks", 3.0)

# --- Catalog ---
catalog = ItemCatalog()
catalog.add_item(burger)
catalog.add_item(soda)
catalog.add_item(brownie)
catalog.add_item(water)

print("=== All Items ===")
for item in catalog.get_all_items():
    print(f"  {item.name} | ${item.price} | {item.category} | rating: {item.popularity_rating}")

print("\n=== Drinks Only ===")
for item in catalog.filter_by_category("Drinks"):
    print(f"  {item.name} | ${item.price}")

# --- Customer ---
customer = Customer(id=1, name="Alice")

# --- Transactions ---
order1 = Transaction(items=[burger, soda], customer=customer)
order2 = Transaction(items=[brownie, water], customer=customer)

customer.purchase_history.append(order1)
customer.purchase_history.append(order2)

print(f"\n=== Customer ===")
print(f"  id: {customer.id}, name: {customer.name}")

print(f"\n=== Purchase History ===")
for i, tx in enumerate(customer.get_purchase_history(), 1):
    items_str = ", ".join(item.name for item in tx.items)
    print(f"  Order {i}: [{items_str}] | total: ${tx.compute_total():.2f} | customer: {tx.customer.name}")

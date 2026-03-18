import unittest
from models import Item, ItemCatalog, Transaction, Customer


class TestTransactionTotal(unittest.TestCase):

    def test_calculate_total_with_multiple_items(self):
        items = [Item("Burger", 10.00, "Burgers", 4.0),
                 Item("Soda",    5.00, "Drinks",  3.5)]
        self.assertEqual(Transaction(items).compute_total(), 15.00)

    def test_order_total_is_zero_when_empty(self):
        self.assertEqual(Transaction([]).compute_total(), 0.0)

    def test_single_item_total_equals_its_price(self):
        item = Item("Brownie", 3.99, "Desserts", 4.1)
        self.assertAlmostEqual(Transaction([item]).compute_total(), 3.99, places=2)


class TestItemCatalogFilter(unittest.TestCase):

    def setUp(self):
        self.catalog = ItemCatalog()
        self.catalog.add_item(Item("Lemonade",    2.99, "Drinks",   4.7))
        self.catalog.add_item(Item("Iced Coffee", 3.49, "Drinks",   4.2))
        self.catalog.add_item(Item("Burger",      8.99, "Burgers",  4.5))

    def test_filter_returns_only_matching_category(self):
        results = self.catalog.filter_by_category("Drinks")
        self.assertGreater(len(results), 0)
        self.assertTrue(all(item.category == "Drinks" for item in results))

    def test_filter_returns_correct_count(self):
        self.assertEqual(len(self.catalog.filter_by_category("Drinks")), 2)

    def test_filter_nonexistent_category_returns_empty_list(self):
        self.assertEqual(self.catalog.filter_by_category("Sushi"), [])

    def test_get_all_items_returns_every_item(self):
        self.assertEqual(len(self.catalog.get_all_items()), 3)


class TestItemCatalogSorting(unittest.TestCase):

    def setUp(self):
        self.catalog = ItemCatalog()
        self.catalog.add_item(Item("Cake",   5.99, "Desserts", 4.9))
        self.catalog.add_item(Item("Soda",   1.99, "Drinks",   3.0))
        self.catalog.add_item(Item("Burger", 8.99, "Burgers",  4.5))

    def test_sort_by_price_ascending(self):
        prices = [i.price for i in self.catalog.get_items_sorted_by_price(desc=False)]
        self.assertEqual(prices, [1.99, 5.99, 8.99])

    def test_sort_by_price_descending(self):
        prices = [i.price for i in self.catalog.get_items_sorted_by_price(desc=True)]
        self.assertEqual(prices, sorted(prices, reverse=True))

    def test_sort_by_popularity_descending_by_default(self):
        ratings = [i.popularity_rating for i in self.catalog.get_items_sorted_by_popularity()]
        self.assertEqual(ratings, sorted(ratings, reverse=True))


class TestCustomerHistory(unittest.TestCase):

    def test_total_spent_across_multiple_orders(self):
        customer = Customer(id=1, name="Alice")
        customer.purchase_history.append(Transaction([Item("Burger", 10.00, "Burgers", 4.0)]))
        customer.purchase_history.append(Transaction([Item("Soda",    5.00, "Drinks",  3.5)]))
        self.assertEqual(customer.get_total_spent(), 15.00)

    def test_total_spent_is_zero_with_no_orders(self):
        customer = Customer(id=2, name="Bob")
        self.assertEqual(customer.get_total_spent(), 0.0)

    def test_purchase_history_grows_with_each_transaction(self):
        customer = Customer(id=3, name="Carol")
        customer.purchase_history.append(Transaction([Item("Cake",   5.99, "Desserts", 4.9)]))
        customer.purchase_history.append(Transaction([Item("Burger", 8.99, "Burgers",  4.5)]))
        self.assertEqual(len(customer.purchase_history), 2)


if __name__ == "__main__":
    unittest.main()

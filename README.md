# ByteBites

A Python domain model for a food ordering system. ByteBites defines the core backend classes that represent customers, menu items, catalogs, and transactions — along with a full test suite covering key behaviors and edge cases.

---

## Project Structure

```
bytebites_tinker_activity/
├── models.py          # Core domain classes
├── test_bytebites.py  # Unit test suite
├── bytebites_spec.md  # Original feature spec
└── bytebites_design.md  # UML class diagram
```

---

## Domain Model

Four classes make up the core of the system:

| Class | Responsibility |
|---|---|
| `Customer` | Stores customer identity and purchase history |
| `Item` | Represents a single food or drink with name, price, category, and popularity rating |
| `ItemCatalog` | Manages the full menu — add, retrieve, filter, and sort items |
| `Transaction` | Groups items into an order and computes the total cost |

### Class Diagram

```
┌─────────────────────────────────┐
│            Customer             │
├─────────────────────────────────┤
│ - id: int                       │
│ - name: str                     │
│ - purchase_history: List[Transaction] │
├─────────────────────────────────┤
│ + get_purchase_history(): List  │
│ + get_total_spent(): float      │
└─────────────────┬───────────────┘
                  │ 1
                  │ has many
                  │ *
                  ▼
┌─────────────────────────────────┐
│           Transaction           │
├─────────────────────────────────┤
│ - items: List[Item]             │
│ - customer: Customer (optional) │
├─────────────────────────────────┤
│ + compute_total(): float        │
└─────────────────┬───────────────┘
                  │ 1
                  │ contains
                  │ *
                  ▼
┌─────────────────────────────────┐
│              Item               │
├─────────────────────────────────┤
│ - name: str                     │
│ - price: float                  │
│ - category: str                 │
│ - popularity_rating: float      │
└─────────────────────────────────┘
                  ▲
                  │ * (aggregates)
                  │
┌─────────────────────────────────┐
│           ItemCatalog           │
├─────────────────────────────────┤
│ - items: List[Item]             │
├─────────────────────────────────┤
│ + add_item(item)                │
│ + get_all_items(): List[Item]   │
│ + filter_by_category(category)  │
│ + get_items_sorted_by_price()   │
│ + get_items_sorted_by_popularity() │
└─────────────────────────────────┘
```

### Relationships

- `Customer` → `Transaction`: one-to-many (a customer has many past transactions)
- `Transaction` → `Item`: one-to-many (a transaction contains one or more items)
- `ItemCatalog` → `Item`: aggregation (the catalog manages items; items exist independently)
- `Transaction` → `Customer`: optional back-reference

---

## Quickstart

No dependencies required — uses Python's standard library only.

```bash
# Run the demo scenario
python models.py

# Run the test suite
python -m unittest test_bytebites -v
```

---

## Running Tests

```
$ python -m unittest test_bytebites -v

test_purchase_history_grows_with_each_transaction ... ok
test_total_spent_across_multiple_orders ... ok
test_total_spent_is_zero_with_no_orders ... ok
test_filter_nonexistent_category_returns_empty_list ... ok
test_filter_returns_correct_count ... ok
test_filter_returns_only_matching_category ... ok
test_get_all_items_returns_every_item ... ok
test_sort_by_popularity_descending_by_default ... ok
test_sort_by_price_ascending ... ok
test_sort_by_price_descending ... ok
test_calculate_total_with_multiple_items ... ok
test_order_total_is_zero_when_empty ... ok
test_single_item_total_equals_its_price ... ok

Ran 13 tests in 0.001s — OK
```

### Test Coverage

| Area | Tests |
|---|---|
| Order totals (single, multiple, empty) | `TestTransactionTotal` |
| Category filtering | `TestItemCatalogFilter` |
| Sorting by price and popularity | `TestItemCatalogSorting` |
| Customer spend tracking and history growth | `TestCustomerHistory` |

---

## Requirements

- Python 3.10+
- No external packages

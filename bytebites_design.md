# ByteBites Domain Model — UML Class Diagram

```
┌─────────────────────────────────┐
│            Customer             │
├─────────────────────────────────┤
│ - id: int                       │
│ - name: str                     │
│ - purchase_history: List[Transaction] │
├─────────────────────────────────┤
│ + get_purchase_history(): List  │
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
│ + add_item(item: Item): void    │
│ + get_all_items(): List[Item]   │
│ + filter_by_category(cat: str)  │
│   : List[Item]                  │
└─────────────────────────────────┘
```

## Relationships

- `Customer` → `Transaction`: one-to-many (a customer has many past transactions)
- `Transaction` → `Item`: one-to-many (a transaction contains one or more items)
- `ItemCatalog` → `Item`: aggregation (the catalog manages a collection of items; items exist independently)
- `Transaction` → `Customer`: optional back-reference (a transaction can optionally know which customer placed it)

# Inventory Insurance Stream Problem

## Overview

You are given a stream of operations representing inventory changes.

After each operation, compute the total insurance value of all items.

This is a classic state-mutation problem:
1. Maintain internal state
2. Apply operations sequentially
3. Recompute a derived metric after each step


---

# Data Model

Each item is identified by `itemId`.

For each item, track:

- qty (integer >= 0)
- categoryId (integer)
- unitValue (integer)


---

# Category Multiplier

Insurance depends on category risk.

Example:

category_multiplier = {
    10: 1,
    20: 2,
    30: 5
}


---

# Insurance Formula

After each operation:

Insurance = SUM over all items of:

    qty * unitValue * category_multiplier[categoryId]


---

# Input Format

You are given:

ops = [
    ["RECEIVE","A",10,10,100],
    ["CHECKOUT","A",3],
    ...
]

Each operation is an array.
The first element determines the operation type.


---

# Operations

## 1. RECEIVE

["RECEIVE", itemId, categoryId, qty, unitValue]

If item does NOT exist:
    Create it.

If item exists:
    Increase quantity only.
    Do NOT overwrite categoryId or unitValue.


---

## 2. CHECKOUT

["CHECKOUT", itemId, qty]

If sufficient quantity exists:
    Subtract qty.

If insufficient:
    Ignore operation.


---

## 3. SELL

["SELL", itemId, qty, salePrice]

If sufficient quantity exists:
    Subtract qty.

If insufficient:
    Ignore operation.

Note:
salePrice does NOT affect insurance.


---

## 4. RECLASSIFY

["RECLASSIFY", itemId, newCategoryId]

If item exists:
    Update categoryId.

Else:
    Ignore.


---

## 5. REVALUE

["REVALUE", itemId, newUnitValue]

If item exists:
    Update unitValue.

Else:
    Ignore.


---

# Required Output

Return a list:

[
  insurance_after_step_1,
  insurance_after_step_2,
  ...
]

Length must equal number of operations.


---

# Implementation Template

## Step 1 — Initialize State

items = {}

Structure:

items[itemId] = (qty, categoryId, unitValue)


---

## Step 2 — Process Operations

For each op in ops:

    operation = op[0]

Use if/elif or match/case.


---

## Step 3 — Mutate State Carefully

Important rules:

- RECEIVE does NOT overwrite category/value for existing items.
- Invalid quantity removals are ignored.
- SELL and CHECKOUT behave the same for quantity.
- RECLASSIFY affects multiplier immediately.
- REVALUE affects all remaining quantity.


---

## Step 4 — Recompute Insurance After Each Operation

total = 0
for qty, categoryId, unitValue in items.values():
    multiplier = category_multiplier.get(categoryId, 1)
    total += qty * unitValue * multiplier

Append total to result list.


---

# Common Interview Mistakes

- Overwriting category or value during RECEIVE
- Forgetting to ignore invalid operations
- Forgetting to apply multiplier after RECLASSIFY
- Forgetting REVALUE affects all remaining qty
- Updating state before validating removal


---

# Complexity

Let:
n = number of operations
k = number of distinct items

Time complexity: O(n * k)
Space complexity: O(k)


---

# Pattern Recognition

This is a "stream of operations maintaining state" problem.

You will see this pattern in:

- Inventory systems
- Banking ledgers
- Order book simulations
- Resource allocation engines

The key skill is:
Correct state mutation with clean invariants.
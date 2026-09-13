def insurance_series(ops, category_multiplier):
    # category_multiplier: dict[int,int], e.g. {10:1, 20:2, 30:5}

    items = {}  # itemId -> (qty, categoryId, unitValue)
    out = []

    def total_insurance():
        return sum(q * v * category_multiplier.get(c, 1)
                   for (q, c, v) in items.values())

    for op in ops:
        match op[0]:
            case "RECEIVE":
                _, item, cat, qty, val = op
                cat, qty, val = int(cat), int(qty), int(val)
                if item in items:
                    q, c, v = items[item]
                    items[item] = (q + qty, c, v)  # only qty changes if already exists
                else:
                    items[item] = (qty, cat, val)

            case "CHECKOUT" | "SELL":
                # SELL has an extra salePrice field; ignore it
                item, qty = op[1], int(op[2])
                if item in items:
                    q, c, v = items[item]
                    if q >= qty:  # invalid ops are ignored
                        items[item] = (q - qty, c, v)

            case "RECLASSIFY":
                _, item, new_cat = op
                if item in items:
                    q, _, v = items[item]
                    items[item] = (q, int(new_cat), v)

            case "REVALUE":
                _, item, new_val = op
                if item in items:
                    q, c, _ = items[item]
                    items[item] = (q, c, int(new_val))

            case _:
                raise ValueError(f"Unknown operation: {op[0]}")

        out.append(total_insurance())

    return out

# ---------------- MAIN BLOCK ----------------

if __name__ == "__main__":

    ops = [
        ["RECEIVE","A",10,10,100],
        ["RECEIVE","B",20,4,250],
        ["CHECKOUT","A",3],
        ["RECLASSIFY","A",30],
        ["SELL","B",1,300],
        ["REVALUE","A",120],
        ["CHECKOUT","B",10],
        ["RECEIVE","C",10,7,80],
        ["RECLASSIFY","C",20],
        ["SELL","A",2,500]
    ]

    category_multiplier = {
        10: 1,
        20: 2,
        30: 5
    }

    output = insurance_series(ops, category_multiplier)
    print(output)
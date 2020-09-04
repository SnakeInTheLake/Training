def cost(capacity: [int, float], items: list) -> float:
    total = 0
    while capacity > 0:
        if not items:
            break
        most_valuable = items.pop(0)
        if most_valuable[1] <= capacity:
            total += most_valuable[0] * most_valuable[1]
            capacity -= most_valuable[1]
        else:
            total += capacity * most_valuable[0]
            capacity = 0

    return total


number_of_items, capacity = map(int, input().split())

item_list = []
for i in range(number_of_items):
    price, weight = map(int, input().split())
    item_list.append([price / weight, weight])

item_list.sort(key=lambda x: x[0], reverse=True)

total = cost(capacity, item_list)
print(format(total, '.3f'))

